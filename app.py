import streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

# --- CONFIGURAÇÃO ---
BASE_DIR = "radio online"
TEMP_DIR = os.path.join(BASE_DIR, "downloads_temp")
LISTA_SALVA = os.path.join(BASE_DIR, "fila_radio.json")

for d in [BASE_DIR, TEMP_DIR]:
    if not os.path.exists(d): os.makedirs(d)

def limpar_nome(nome):
    nome = re.sub(r'[\\/*?:"<>|#]', "", nome)
    return nome.strip()

if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        try:
            with open(LISTA_SALVA, "r", encoding="utf-8") as f:
                st.session_state.fila_nuvem = json.load(f)
        except: st.session_state.fila_nuvem = []
    else: st.session_state.fila_nuvem = []

def salvar_fila():
    with open(LISTA_SALVA, "w", encoding="utf-8") as f:
        json.dump(st.session_state.fila_nuvem, f)

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻")
st.title("📻 Console Rádio Hub + Prévia")

# --- BUSCA COM PRÉVIA ---
busca = st.text_input("Cole o Link ou Nome da Música:", placeholder="Ex: Matheus & Kauan Fase de Cura")

if st.button("🔍 BUSCAR MÚSICA", use_container_width=True):
    if busca:
        with st.spinner("Buscando áudio..."):
            ydl_opts_busca = {
                'format': 'bestaudio/best', # Busca o melhor áudio para a prévia
                'quiet': True,
                'default_search': 'ytsearch1',
                'nocheckcertificate': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts_busca) as ydl:
                    info = ydl.extract_info(busca, download=False)
                    res = info['entries'][0] if 'entries' in info else info
                    
                    titulo = limpar_nome(res.get('title', '
