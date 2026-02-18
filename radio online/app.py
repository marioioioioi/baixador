import streamlit as st
import yt_dlp
import os
import time

# Otimização para Celeron N4020 e 4GB de RAM
st.set_page_config(page_title="Rádio Hub - Console", page_icon="📻", layout="wide")

# Inicialização da fila de memória
if 'fila_joca' not in st.session_state:
    st.session_state.fila_joca = []

# Diretório de salvamento
DOWNLOAD_DIR = "Musicas_da_Radio"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# --- FUNÇÃO PARA FORMATAR TAMANHO DE ARQUIVO ---
def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024: return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} GB"

# --- MODAL DE CONFIRMAÇÃO (DIALOG) ---
@st.dialog("Confirmar Música para a Rádio")
def modal_confirmacao(video_info):
    st.write(f"### 🎵 {video_info.get('title')}")
    
    col_thumb, col_play = st.columns([1, 1])
    
    with col_thumb:
        if video_info.get('thumbnail'):
            st.image(video_info.get('thumbnail'), use_container_width=True)
    
    with col_play:
        st.write("**Ouvir prévia:**")
        # Streaming direto do YouTube para o player
        st.audio(video_info.get('url'), format="audio/mp3")
        st.caption("Verifique se o áudio está correto antes de adicionar.")

    st.write("---")
    
    # Qualidade padrão: 320kbps
    qualidade = st.segmented_control(
        "Qualidade do Áudio (kbps):",
        options=["128", "192", "320"],
        default="320"
    )
    
    nome_final = st.text_input("Nome do arquivo no SSD:", value=video_info.get('title'))
    
    col_add, col_can = st.columns(2)
    if col_add.button("✅ ADICIONAR NA FILA", use_container_width=True, type="primary"):
        st.session_state.fila_joca.append({
            'titulo': nome_final,
            'link': video_info.get('webpage_url'),
            'qualidade': qualidade
        })
        st.rerun()
    
    if col_can.button("❌ CANCELAR", use_container_width=True):
        st.rerun()

# --- INTERFACE PRINCIPAL ---
st.title("📻 Console de Transmissão - Rádio Hub")

tab_joca, tab_pro, tab_extrair = st.tabs(["⭐ MODO JOCA", "🚀 MODO AVANÇADO (LOTE)", "📋 EXTRAIR NOMES"])

# --- ABA 1: MODO JOCA ---
with tab_joca:
    with st.form("busca_joca", clear_on_submit=True):
        st.subheader("Buscar Música (Enter para Pesquisar)")
        entrada = st.text_input("Nome da música ou Link:", placeholder="Ex: Zé Neto e Cristiano - Notificação Preferida")
        btn_busca = st.form_submit_button("🔍 BUSCAR NO YOUTUBE", use_container_width=True)

    if btn_busca and entrada:
        with st.spinner("Conectando ao YouTube..."):
            try:
                ydl_search = {
                    'format': 'bestaudio/best',
                    'quiet': True,
                    'default_search': 'ytsearch1',
                    'noplaylist': True,
                    'nocheckcertificate': True
                }
                with yt_dlp.YoutubeDL(ydl_search) as ydl:
                    info = ydl.extract_info(entrada, download=False)
                    if not info or ('entries' in info and len(info['entries']) == 0):
                        st.error("Não encontramos essa música.")
                    else:
                        video = info['entries'][0] if 'entries' in info else info
                        modal_confirmacao(video)
            except Exception as e:
                st.error(f"Erro na busca: {e}")

    # Exibição da Fila
    if st.session_state.fila_joca:
        st.divider()
        col_t1, col_t2 = st.columns([3, 1])
        col_t1.subheader(f"📋 Fila de Espera ({len(st.session_state.fila_joca)} músicas)")
        
        if col_t2.button("🗑️ LIMPAR TODA A FILA", use_container_width=True):
            st.session_state.fila_joca = []
            st.rerun()

        for idx, m in enumerate(st.session_state.fila_joca):
            with st.container(border=True):
                c1, c2, c3 = st.columns([4, 1, 0.5])
                c1.write(f"**{idx+1}. {m['titulo']}**")
                c2.caption(f"🎧 {m['qualidade']}kbps")
                if c3.button("❌", key=f"del_{idx}"):
                    st.session_state.fila_joca.pop(idx)
                    st.rerun()
        
        st.write("")
        if st.button("🚀 INICIAR DOWNLOAD DE TODA A FILA", type="primary", use_container_width=True):
            total_fila = len(st.session_state.fila_joca)
            total_bytes = 0
            prog_bar = st.progress(0)
            status_container = st.empty()
            detalhes_container = st.empty()
            
            for i, m in enumerate(st.session_state.fila_joca):
                num = i + 1
                status_container.markdown(f"**Baixando ({num}/{total_fila}):** `{m['titulo']}`")
                
                opts = {
                    'format': 'bestaudio/best',
                    'ffmpeg_location': './ffmpeg.exe',
                    'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': m['qualidade']}],
                    'outtmpl': f'{DOWNLOAD_DIR}/{m["titulo"]}.%(ext)s',
                    'quiet': True
                }
                
                try:
                    with yt_dlp.YoutubeDL(opts) as ydl:
                        info_dl = ydl.extract_info(m['link'], download=True)
                        size = info_dl.get('filesize') or info_dl.get('filesize_approx') or 0
                        total_bytes += size
                        detalhes_container.info(f"📊 Tamanho: {format_size(size)} | Qualidade: {m['qualidade']}kbps")
                    prog_bar.progress(num / total_fila)
                except:
                    st.error(f"Erro no download: {m['titulo']}")
            
            st.balloons()
            status_container.success(f"✅ Download Concluído! Músicas salvas em '{DOWNLOAD_DIR}'.")
            detalhes_container.success(f"📊 **Recibo Final:** Total de **{format_size(total_bytes)}** baixados para o SSD.")
            st.session_state.fila_joca = []

# --- ABA 2: MODO AVANÇADO (LOTE) ---
with tab_pro:
    st.subheader("Processamento em Massa (320kbps)")
    lista_txt = st.text_area("Cole sua lista numerada ou de links:", height=300, placeholder="1. Música A\n2. Música B...")
    
    if st.button("🔥 INICIAR LOTE COMPLETO", use_container_width=True):
        linhas = [l.strip() for l in lista_txt.split('\n') if l.strip()]
        if linhas:
            pb_l = st.progress(0)
            st_l = st.empty()
            total_l = 0
            for i, linha in enumerate(linhas):
                nome_l = linha.split('. ', 1)[-1] if '. ' in linha[:5] else linha
                st_l.markdown(f"**Processando ({i+1}/{len(linhas)}):** `{nome_l}`")
                opts_l = {'format': 'bestaudio/best', 'ffmpeg_location': './ffmpeg.exe', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '320'}], 'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s', 'default_search': 'ytsearch1', 'quiet': True}
                try:
                    with yt_dlp.YoutubeDL(opts_l) as ydl:
                        info_l = ydl.extract_info(nome_l, download=True)
                        total_l += info_l.get('filesize') or info_l.get('filesize_approx') or 0
                except: pass
                pb_l.progress((i + 1) / len(linhas))
            st_l.success(f"✅ Lote finalizado! Total: {format_size(total_l)}")

# --- ABA 3: EXTRAIR NOMES ---
with tab_extrair:
    url_p = st.text_input("Link da Playlist do YouTube:")
    if st.button("Gerar Lista TXT"):
        with st.spinner("Lendo..."):
            with yt_dlp.YoutubeDL({'extract_flat': True, 'quiet': True}) as ydl:
                res = ydl.extract_info(url_p, download=False)
                txt = "\n".join([f"{e['title']}" for e in res['entries'] if e])
                st.download_button("💾 Baixar lista.txt", txt, file_name="lista_radio.txt")
                st.text_area("Nomes extraídos:", txt, height=200)