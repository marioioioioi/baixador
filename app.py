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

# Garante que as pastas existam
for d in [BASE_DIR, TEMP_DIR]:
    if not os.path.exists(d):
        os.makedirs(d)

def limpar_nome(nome):
    """Limpa o nome para evitar erros no Windows e links quebrados"""
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
                    if 'entries' in info:
                        res = info['entries'][0]
                    else:
                        res = info
