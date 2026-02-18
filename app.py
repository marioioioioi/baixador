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

# --- ESTADO DA SESSÃO ---
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

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻")
st.title("📻 Console Rádio Hub + Prévia")

# --- BUSCA COM PRÉVIA ---
busca = st.text_input("Busque pelo nome ou cole o link do YouTube:", placeholder="Ex: Matheus & Kauan Fase de Cura")

if st.button("🔍 PESQUISAR MÚSICA", use_container_width=True):
    if busca:
        with st.spinner("Buscando áudio..."):
            ydl_opts_busca = {
                'format': 'bestaudio/best',
                'quiet': True,
                'default_search': 'ytsearch1',
                'nocheckcertificate': True,
                'no_warnings': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts_busca) as ydl:
                    info = ydl.extract_info(busca, download=False)
                    res = info['entries'][0] if 'entries' in info else info
                    
                    titulo = limpar_nome(res.get('title', 'Musica'))
                    link_yt = res.get('webpage_url')
                    link_audio_direto = res.get('url')
                    
                    # Armazena temporariamente para o botão de confirmação
                    st.session_state.temp_song = {
                        'titulo': titulo, 
                        'link': link_yt,
                        'previa': link_audio_direto
                    }
                    
                    st.write(f"### 🎵 Resultado: {titulo}")
                    st.audio(link_audio_direto, format="audio/mp3")
            except Exception as e:
                st.error(f"Erro ao buscar música: {e}")

# Botão para adicionar (aparece só se houver resultado)
if 'temp_song' in
