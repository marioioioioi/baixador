import streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻", layout="wide")

TEMP_DIR = "temp_radio"
LISTA_SALVA = "fila_radio.json"

if not os.path.exists(TEMP_DIR): 
    os.makedirs(TEMP_DIR)

# Função para limpar nomes de arquivos (Essencial para não dar erro)
def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

def salvar_fila():
    with open(LISTA_SALVA, "w") as f: json.dump(st.session_state.fila_nuvem, f)

# --- MODAL MODO JOCA ---
@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    nome_f = st.text_input("Nome do arquivo:", value=video_info.get('title'))
    if st.button("✅ ADICIONAR", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({
            'titulo': limpar_nome(nome_f), 
            'link': video_info.get('webpage_url') or video_info.get('url')
        })
        salvar_fila()
        st.rerun()

st.title("📻 Console Rádio Hub 24h")

tab_joca, tab_lote, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 LOTE AVANÇADO", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    busca = st.text_input("Buscar música:")
    if st.button("🔍 PESQUISAR", use_container_width=True):
        with st.spinner("Buscando..."):
            opts = {'format':'bestaudio/best','quiet':True,'default_search':'ytsearch1','noplaylist':True}
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(busca, download=False)
                res = info['entries'][0] if 'entries' in info else info
                modal_confirmacao(res)

    if st.session_state.fila_nuvem:
        st.divider()
        c1, c2 = st.columns([3, 1])
        c1.subheader(f"📋 Fila ({len(st.session_state.fila_nuvem)})")
        if c2.button("🗑️ LIMPAR TUDO"):
            st.session_state.fila_nuvem = []; salvar_fila(); st.rerun()

        for idx, m in enumerate(st.session_state.fila_nuvem):
            with st.container(border=True):
                col_m, col_b = st.columns([5, 1])
                col_m.write(f"🎵 {m['titulo']}")
                if col_b.button("❌", key=f"del_{idx}"):
                    st.session_state.fila_nuvem.pop(idx); salvar_fila(); st.rerun()

        if st.button("🚀 GERAR ZIP DA FILA", type="primary", use_container_width=True):
            if os.path.exists(TEMP_DIR): shutil.rmtree(TEMP_DIR)
            os.makedirs(TEMP_DIR)
            
            pb = st.progress(0)
            st_txt = st.empty()
            
            for i, m in enumerate(st.session_state.fila_nuvem):
                st_txt.write(f"📥 Convertendo: {m['titulo']}")
                opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192', # 192kbps é mais rápido e estável
                    }],
                    'outtmpl': f'{TEMP_DIR}/{m["titulo"]}.%(ext)s',
                    'quiet': True,
                    'noplaylist': True
                }
                try:
                    with yt_dlp.YoutubeDL(opts) as ydl:
                        ydl.download([m['link']])
                except Exception as e:
                    st.error(f"Erro em {m['titulo']}: {e}")
                
                pb.progress((i+1)/len(st.session_state.fila_nuvem))
            
            # Criar ZIP
            buf = BytesIO()
            with zipfile.ZipFile(buf, "w") as z:
                for arq in os.listdir(TEMP_DIR):
                    z.write(os.path.join(TEMP_DIR, arq), arq)
            
            if len(os.listdir(TEMP_DIR)) > 0:
                st_txt.success("✅ Tudo pronto!")
                st.download_button("💾 BAIXAR ZIP AGORA", buf.getvalue(), file_name="radio_joca.zip", use_container_width=True)
            else:
                st.error("Nenhum arquivo foi baixado. Verifique se o FFmpeg está instalado.")

# --- ABA 2: LOTE AVANÇADO ---
with tab_lote:
    txt_area = st.text_area("Cole sua lista (um por linha):", height=200)
    if st.button("🔥 BAIXAR TUDO EM ZIP", use_container_width=True):
        musicas = [l.strip() for l in txt_area.split('\n') if l.strip()]
        if musicas:
            if os.path.exists(TEMP_DIR): shutil.rmtree(TEMP_DIR)
            os.makedirs(TEMP_DIR)
            pb_l = st.progress(0)
            st_l = st.empty()
            for i, m in enumerate(musicas):
                nome_limpo = limpar_nome(m.split('. ', 1)[-1] if '. ' in m[:5] else m)
                st_l.write(f"📥 Baixando: {nome_limpo}")
                opts_l = {
                    'format':'bestaudio/best',
                    'postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'192'}],
                    'outtmpl':f'{TEMP_DIR}/{nome_limpo}.%(ext)s',
                    'default_search':'ytsearch1',
                    'quiet':True
                }
                try:
                    with yt_dlp.YoutubeDL(opts_l) as ydl: ydl.download([m])
                except Exception as e: st.warning(f"Falha ao baixar {m}")
                pb_l.progress((i+1)/len(musicas))
            
            buf_l = BytesIO()
            with zipfile.ZipFile(buf_l, "w") as z:
                for arq in os.listdir(TEMP_DIR): z.write(os.path.join(TEMP_DIR, arq), arq)
            st.download_button("💾 SALVAR ZIP DO LOTE", buf_l.getvalue(), file_name="lote_radio.zip", use_container_width=True)

# --- ABA 3: EXTRAIR NOMES ---
with tab_extrair:
    url_p = st.text_input("Link da Playlist:")
    if st.button("GERAR LISTA"):
        with st.spinner("Lendo..."):
            with yt_dlp.YoutubeDL({'extract_flat':True,'quiet':True}) as ydl:
                res = ydl.extract_info(url_p, download=False)
                nomes = "\n".join([f"{e['title']}" for e in res['entries'] if e])
                st.text_area("Resultado (Copie e cole na aba LOTE):", nomes, height=200)
