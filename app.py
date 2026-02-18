import streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

# --- CONFIGURAÇÃO DE DIRETÓRIOS ---
BASE_DIR = "radio online"
TEMP_DIR = os.path.join(BASE_DIR, "downloads_temp")
LISTA_SALVA = os.path.join(BASE_DIR, "fila_radio.json")

for d in [BASE_DIR, TEMP_DIR]:
    if not os.path.exists(d):
        os.makedirs(d)

def limpar_nome(nome):
    nome = re.sub(r'[\\/*?:"<>|#]', "", nome)
    return nome.strip()

# --- INICIALIZAÇÃO DO ESTADO ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        try:
            with open(LISTA_SALVA, "r", encoding="utf-8") as f:
                st.session_state.fila_nuvem = json.load(f)
        except:
            st.session_state.fila_nuvem = []
    else:
        st.session_state.fila_nuvem = []

def salvar_fila():
    with open(LISTA_SALVA, "w", encoding="utf-8") as f:
        json.dump(st.session_state.fila_nuvem, f)

# --- INTERFACE ---
st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻")
st.title("📻 Console Rádio Hub (Versão Anti-Bloqueio)")

# --- ABA DE BUSCA ---
busca = st.text_input("Cole o Link do YouTube ou Nome da Música:", placeholder="Ex: Matheus & Kauan Fase de Cura")

if st.button("🔍 ADICIONAR À FILA", use_container_width=True):
    if busca:
        with st.spinner("Buscando no YouTube..."):
            ydl_opts_busca = {
                'format': 'bestaudio',
                'quiet': True,
                'default_search': 'ytsearch1',
                'nocheckcertificate': True,
                'no_warnings': True,
                'extract_flat': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts_busca) as ydl:
                    info = ydl.extract_info(busca, download=False)
                    if info:
                        if 'entries' in info:
                            res = info['entries'][0]
                        else:
                            res = info
                        
                        titulo = limpar_nome(res.get('title', 'Musica_Sem_Nome'))
                        link = res.get('webpage_url') or res.get('url')
                        
                        st.session_state.fila_nuvem.append({'titulo': titulo, 'link': link})
                        salvar_fila()
                        st.success(f"✅ Adicionado: {titulo}")
                        st.rerun()
            except Exception as e:
                st.error(f"Erro ao buscar: {e}")

# --- EXIBIÇÃO DA FILA ---
if st.session_state.fila_nuvem:
    st.divider()
    st.subheader(f"📋 Músicas na Fila ({len(st.session_state.fila_nuvem)})")
    
    for idx, m in enumerate(st.session_state.fila_nuvem):
        c1, c2 = st.columns([5, 1])
        c1.write(f"🎵 {m['titulo']}")
        if c2.button("❌", key=f"del_{idx}"):
            st.session_state.fila_nuvem.pop(idx)
            salvar_fila()
            st.rerun()

    st.divider()
    
    # --- BOTÃO DE DOWNLOAD ---
    if st.button("🚀 INICIAR DOWNLOAD DE TUDO (ZIP)", type="primary", use_container_width=True):
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
        os.makedirs(TEMP_DIR)
        
        prog = st.progress(0)
        status = st.empty()
        baixados = 0
        
        for i, m in enumerate(st.session_state.fila_nuvem):
            status.write(f"📥 Baixando ({i+1}/{len(st.session_state.fila_nuvem)}): {m['titulo']}")
            
            opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{TEMP_DIR}/{m["titulo"]}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
                'http_chunk_size': 1048576, 
                'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            }
            
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([m['link']])
                    baixados += 1
            except Exception as e:
                st.error(f"❌ Erro em {m['titulo']}: {e}")
            
            prog.progress((i + 1) / len(st.session_state.fila_nuvem))
        
        if baixados > 0:
            status.success(f"✅ {baixados} músicas processadas!")
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as z:
                for arq in os.listdir(TEMP_DIR):
                    z.write(os.path.join(TEMP_DIR, arq), arq)
            
            st.download_button(
                label="💾 BAIXAR ARQUIVO ZIP",
                data=zip_buffer.getvalue(),
                file_name="radio_hub_musicas.zip",
                mime="application/zip",
                use_container_width=True
            )

if st.session_state.fila_nuvem:
    if st.button("🗑️ LIMPAR TODA A LISTA"):
        st.session_state.fila_nuvem = []
        salvar_fila()
        st.rerun()
