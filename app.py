import streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻", layout="wide")

# Criar pasta temporária única para esta sessão para evitar conflitos
SESSION_ID = st.runtime.scriptrunner.add_script_run_ctx().getattr('streamlit_script_run_ctx').session_id
TEMP_DIR = f"temp_{SESSION_ID}"
LISTA_SALVA = "fila_radio.json"

if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)

def limpar_nome(nome):
    """ Remove caracteres que causam erro no Windows/Linux """
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

if 'texto_lote' not in st.session_state: st.session_state.texto_lote = ""
if 'busca_termo' not in st.session_state: st.session_state.busca_termo = ""

def salvar_fila():
    with open(LISTA_SALVA, "w") as f: json.dump(st.session_state.fila_nuvem, f)

@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    st.audio(video_info.get('url'), format="audio/mp3")
    nome_f = st.text_input("Nome do arquivo:", value=video_info.get('title'))
    if st.button("✅ ADICIONAR", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({'titulo': limpar_nome(nome_f), 'link': video_info.get('webpage_url') or video_info.get('url')})
        salvar_fila()
        st.rerun()

st.title("📻 Console Rádio Hub 24h")

tab_joca, tab_lote, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 LOTE AVANÇADO", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    busca = st.text_input("Buscar música:", value=st.session_state.busca_termo)
    st.session_state.busca_termo = busca
    
    if st.button("🔍 PESQUISAR", use_container_width=True):
        with st.spinner("Buscando..."):
            with yt_dlp.YoutubeDL({'format':'bestaudio','quiet':True,'default_search':'ytsearch1','noplaylist':True}) as ydl:
                info = ydl.extract_info(busca, download=False)
                modal_confirmacao(info['entries'][0] if 'entries' in info else info)

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
                nome_arq = limpar_nome(m['titulo'])
                st_txt.write(f"📥 Convertendo: {nome_arq}")
                
                # Configuração crucial para garantir que o MP3 seja criado
                opts = {
                    'format': 'bestaudio/best',
                    'postimport streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻", layout="wide")

# Criar pasta temporária única para esta sessão para evitar conflitos
SESSION_ID = st.runtime.scriptrunner.add_script_run_ctx().getattr('streamlit_script_run_ctx').session_id
TEMP_DIR = f"temp_{SESSION_ID}"
LISTA_SALVA = "fila_radio.json"

if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)

def limpar_nome(nome):
    """ Remove caracteres que causam erro no Windows/Linux """
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

if 'texto_lote' not in st.session_state: st.session_state.texto_lote = ""
if 'busca_termo' not in st.session_state: st.session_state.busca_termo = ""

def salvar_fila():
    with open(LISTA_SALVA, "w") as f: json.dump(st.session_state.fila_nuvem, f)

@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    st.audio(video_info.get('url'), format="audio/mp3")
    nome_f = st.text_input("Nome do arquivo:", value=video_info.get('title'))
    if st.button("✅ ADICIONAR", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({'titulo': limpar_nome(nome_f), 'link': video_info.get('webpage_url') or video_info.get('url')})
        salvar_fila()
        st.rerun()

st.title("📻 Console Rádio Hub 24h")

tab_joca, tab_lote, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 LOTE AVANÇADO", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    busca = st.text_input("Buscar música:", value=st.session_state.busca_termo)
    st.session_state.busca_termo = busca
    
    if st.button("🔍 PESQUISAR", use_container_width=True):
        with st.spinner("Buscando..."):
            with yt_dlp.YoutubeDL({'format':'bestaudio','quiet':True,'default_search':'ytsearch1','noplaylist':True}) as ydl:
                info = ydl.extract_info(busca, download=False)
                modal_confirmacao(info['entries'][0] if 'entries' in info else info)

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
                nome_arq = limpar_nome(m['titulo'])
                st_txt.write(f"📥 Convertendo: {nome_arq}")
                
                # Configuração crucial para garantir que o MP3 seja criado
                opts = {
                    'format': 'bestaudio/best',
                    'postimport streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻", layout="wide")

# Criar pasta temporária única para esta sessão para evitar conflitos
SESSION_ID = st.runtime.scriptrunner.add_script_run_ctx().getattr('streamlit_script_run_ctx').session_id
TEMP_DIR = f"temp_{SESSION_ID}"
LISTA_SALVA = "fila_radio.json"

if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)

def limpar_nome(nome):
    """ Remove caracteres que causam erro no Windows/Linux """
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

if 'texto_lote' not in st.session_state: st.session_state.texto_lote = ""
if 'busca_termo' not in st.session_state: st.session_state.busca_termo = ""

def salvar_fila():
    with open(LISTA_SALVA, "w") as f: json.dump(st.session_state.fila_nuvem, f)

@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    st.audio(video_info.get('url'), format="audio/mp3")
    nome_f = st.text_input("Nome do arquivo:", value=video_info.get('title'))
    if st.button("✅ ADICIONAR", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({'titulo': limpar_nome(nome_f), 'link': video_info.get('webpage_url') or video_info.get('url')})
        salvar_fila()
        st.rerun()

st.title("📻 Console Rádio Hub 24h")

tab_joca, tab_lote, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 LOTE AVANÇADO", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    busca = st.text_input("Buscar música:", value=st.session_state.busca_termo)
    st.session_state.busca_termo = busca
    
    if st.button("🔍 PESQUISAR", use_container_width=True):
        with st.spinner("Buscando..."):
            with yt_dlp.YoutubeDL({'format':'bestaudio','quiet':True,'default_search':'ytsearch1','noplaylist':True}) as ydl:
                info = ydl.extract_info(busca, download=False)
                modal_confirmacao(info['entries'][0] if 'entries' in info else info)

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
                nome_arq = limpar_nome(m['titulo'])
                st_txt.write(f"📥 Convertendo: {nome_arq}")
                
                # Configuração crucial para garantir que o MP3 seja criado
                opts = {
                    'format': 'bestaudio/best',
                    'postimport streamlit as st
import yt_dlp
import os
import shutil
import zipfile
import json
import re
from io import BytesIO

st.set_page_config(page_title="Rádio Hub Premium", page_icon="📻", layout="wide")

# Criar pasta temporária única para esta sessão para evitar conflitos
SESSION_ID = st.runtime.scriptrunner.add_script_run_ctx().getattr('streamlit_script_run_ctx').session_id
TEMP_DIR = f"temp_{SESSION_ID}"
LISTA_SALVA = "fila_radio.json"

if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)

def limpar_nome(nome):
    """ Remove caracteres que causam erro no Windows/Linux """
    return re.sub(r'[\\/*?:"<>|]', "", nome)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'fila_nuvem' not in st.session_state:
    if os.path.exists(LISTA_SALVA):
        with open(LISTA_SALVA, "r") as f: st.session_state.fila_nuvem = json.load(f)
    else: st.session_state.fila_nuvem = []

if 'texto_lote' not in st.session_state: st.session_state.texto_lote = ""
if 'busca_termo' not in st.session_state: st.session_state.busca_termo = ""

def salvar_fila():
    with open(LISTA_SALVA, "w") as f: json.dump(st.session_state.fila_nuvem, f)

@st.dialog("Configurar Música")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    st.audio(video_info.get('url'), format="audio/mp3")
    nome_f = st.text_input("Nome do arquivo:", value=video_info.get('title'))
    if st.button("✅ ADICIONAR", use_container_width=True, type="primary"):
        st.session_state.fila_nuvem.append({'titulo': limpar_nome(nome_f), 'link': video_info.get('webpage_url') or video_info.get('url')})
        salvar_fila()
        st.rerun()

st.title("📻 Console Rádio Hub 24h")

tab_joca, tab_lote, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 LOTE AVANÇADO", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    busca = st.text_input("Buscar música:", value=st.session_state.busca_termo)
    st.session_state.busca_termo = busca
    
    if st.button("🔍 PESQUISAR", use_container_width=True):
        with st.spinner("Buscando..."):
            with yt_dlp.YoutubeDL({'format':'bestaudio','quiet':True,'default_search':'ytsearch1','noplaylist':True}) as ydl:
                info = ydl.extract_info(busca, download=False)
                modal_confirmacao(info['entries'][0] if 'entries' in info else info)

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
                nome_arq = limpar_nome(m['titulo'])
                st_txt.write(f"📥 Convertendo: {nome_arq}")
                
                # Configuração crucial para garantir que o MP3 seja criado
                opts = {
                    'format': 'bestaudio/best',
                    'post
