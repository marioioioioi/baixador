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
    # Remove emojis e caracteres que o YouTube/Windows odeiam
    nome = re.sub(r'[\\/*?:"<>|#]', "", nome)
    return nome.strip()

if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r", encoding="utf-8") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

def salvar_fila():
    with open(LISTA_SALVA, "w", encoding="utf-8") as f: json.dump(st.session_state.fila_nuvem, f)

st.title("📻 Console Rádio Hub (Anti-Bloqueio)")

# --- BUSCA ---
busca = st.text_input("Cole o link ou nome da música:")
if st.button("🔍 ADICIONAR À FILA"):
    with st.spinner("Buscando informações..."):
        # Otimizado para evitar o 403 já na busca
        ydl_opts_busca = {
            'format': 'bestaudio', 
            'quiet': True, 
            'default_search': 'ytsearch1',
            'nocheckcertificate': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts_busca) as ydl:
                info = ydl.extract_info(busca, download=False)
                res = info['entries'][0] if 'entries' in info else info
                titulo_limpo = limpar_nome(res.get('title'))
                st.session_state.fila_nuvem.append({'titulo': titulo_limpo, 'link': res.get('webpage_url')})
                salvar_fila()
                st.success(f"Adicionado: {titulo_limpo}")
        except Exception as e:
            st.error(f"Erro na busca: {e}")

# --- FILA ---
if st.session_state.fila_nuvem:
    st.divider()
    for idx, m in enumerate(st.session_state.fila_nuvem):
        c1, c2 = st.columns([5, 1])
        c1.write(f"🎵 {m['titulo']}")
        if c2.button("❌", key=f"del_{idx}"):
            st.session_state.fila_nuvem.pop(idx); salvar_fila(); st.rerun()

    if st.button("🚀 BAIXAR TUDO (CORRIGIR ERRO 403)", type="primary", use_container_width=True):
        if os.path.exists(TEMP_DIR): shutil.rmtree(TEMP_DIR)
        os.makedirs(TEMP_DIR)
        
        prog = st.progress(0)
        status = st.empty()
        
        baixados = 0
        for i, m in enumerate(st.session_state.fila_nuvem):
            status.write(f"📥 Tentando baixar: {m['titulo']}")
            
            opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{TEMP_DIR}/{m["titulo"]}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
                'nocheckcertificate': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'referer': 'https://www.youtube.com/',
            }
            
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([m['link']])
                    baixados += 1
            except Exception as e:
                st.error(f"Falhou: {m['titulo']}. Motivo: {e}")
            
            prog.progress((i + 1) / len(st.session_state.fila_nuvem))
        
        if baixados > 0:
            buf = BytesIO()
            with zipfile.ZipFile(buf, "w") as z:
                for arq in os.listdir(TEMP_DIR):
                    z.write(os.path.join(TEMP_DIR, arq), arq)
            st.download_button("💾 BAIXAR ZIP COMPLETO", buf.getvalue(), file_name="radio_hub.zip", use_container_width=True)
