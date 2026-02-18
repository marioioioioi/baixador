import streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

# --- CONFIGURAÇÃO DE DIRETÓRIOS ---
# Nome da sua pasta conforme solicitado
BASE_DIR = "radio online"
TEMP_DIR = os.path.join(BASE_DIR, "downloads_temp")
LISTA_SALVA = os.path.join(BASE_DIR, "fila_radio.json")

# Cria as pastas se não existirem
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def limpar_nome(nome):
    """Remove caracteres que impedem o download no Windows/Linux"""
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- MEMÓRIA DO SISTEMA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r", encoding="utf-8") as f: 
            st.session_state.fila_nuvem = json.load(f)
    else: 
        st.session_state.fila_nuvem = []

def salvar_fila():
    with open(LISTA_SALVA, "w", encoding="utf-8") as f: 
        json.dump(st.session_state.fila_nuvem, f)

# --- MODAL DE ADIÇÃO ---
@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    nome_sugerido = limpar_nome(video_info.get('title'))
    nome_f = st.text_input("Nome do arquivo final:", value=nome_sugerido)
    
    if st.button("✅ ADICIONAR À LISTA", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({
            'titulo': nome_f, 
            'link': video_info.get('webpage_url') or video_info.get('url')
        })
        salvar_fila()
        st.rerun()

# --- INTERFACE ---
st.title("📻 Console Rádio Hub - " + BASE_DIR)

tab1, tab2 = st.tabs(["⭐ Modo Busca", "🚀 Baixar em Lote"])

with tab1:
    busca = st.text_input("O que quer ouvir?", placeholder="Nome da música ou link...")
    if st.button("🔍 BUSCAR"):
        with st.spinner("Pesquisando..."):
            ydl_opts = {'format': 'bestaudio', 'quiet': True, 'default_search': 'ytsearch1'}
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(busca, download=False)
                    res = info['entries'][0] if 'entries' in info else info
                    modal_confirmacao(res)
            except Exception as e:
                st.error(f"Erro na busca: {e}")

    if st.session_state.fila_nuvem:
        st.divider()
        st.subheader(f"📋 Fila atual ({len(st.session_state.fila_nuvem)})")
        
        for idx, m in enumerate(st.session_state.fila_nuvem):
            c1, c2 = st.columns([5, 1])
            c1.write(f"🎵 {m['titulo']}")
            if c2.button("❌", key=f"del_{idx}"):
                st.session_state.fila_nuvem.pop(idx); salvar_fila(); st.rerun()

        if st.button("🚀 BAIXAR TUDO AGORA", type="primary", use_container_width=True):
            # Limpa a pasta temporária antes de começar
            if os.path.exists(TEMP_DIR): shutil.rmtree(TEMP_DIR)
            os.makedirs(TEMP_DIR)
            
            prog = st.progress(0)
            status = st.empty()
            
            baixados = 0
            for i, m in enumerate(st.session_state.fila_nuvem):
                status.write(f"📥 Baixando: {m['titulo']}")
                
                # OPÇÕES DE DOWNLOAD
                opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': f'{TEMP_DIR}/{m["titulo"]}.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'quiet': True,
                }
                
                try:
                    with yt_dlp.YoutubeDL(opts) as ydl:
                        ydl.download([m['link']])
                        baixados += 1
                except Exception as e:
                    st.error(f"Erro ao baixar {m['titulo']}: {e}")
                
                prog.progress((i + 1) / len(st.session_state.fila_nuvem))
            
            # CRIAR ZIP
            if baixados > 0:
                zip_path = os.path.join(BASE_DIR, "radio_hub.zip")
                buf = BytesIO()
                with zipfile.ZipFile(buf, "w") as z:
                    for arq in os.listdir(TEMP_DIR):
                        z.write(os.path.join(TEMP_DIR, arq), arq)
                
                status.success(f"✅ {baixados} músicas prontas!")
                st.download_button("💾 SALVAR ARQUIVO ZIP", buf.getvalue(), file_name="musicas_radio.zip", use_container_width=True)
            else:
                st.error("Nenhuma música foi baixada. O YouTube pode ter bloqueado ou falta o FFmpeg.")

with tab2:
    lote = st.text_area("Cole os nomes ou links (um por linha):")
    if st.button("🔥 PROCESSAR LOTE"):
        st.info("O processo de lote seguirá a mesma lógica da aba principal.")
        # (A lógica de lote pode ser repetida aqui usando a mesma função de download acima)
