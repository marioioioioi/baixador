import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="Portal Paroquial", page_icon="⛪", layout="wide")

# --- CSS PROFISSIONAL (BLOCOS CURTOS PARA EVITAR ERRO) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;700&display=swap');
    .main { background-color: #f8f9fa; }
    .hero {
        background: linear-gradient(135deg, #002d5b 0%, #0056b3 100%);
        color: #FFD700; padding: 50px; border-radius: 20px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin-bottom: 25px;
    }
    .hero h1 { font-family: 'Cinzel', serif; font-size: 3rem !important; }
    .card-liturgia {
        background: white; border-left: 6px solid #FFD700; padding: 20px;
        border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("""
<div class="hero">
    <h1>PARÓQUIA NOSSA SENHORA APARECIDA</h1>
    <p style="color:white; font-family:'Montserrat';">Comunidade de Fé, Oração e Evangelização</p>
</div>
""", unsafe_allow_html=True)

# --- COLUNAS PRINCIPAIS ---
col_missa, col_lit = st.columns([1.5, 1])

with col_missa:
    st.subheader("🔴 Transmissão e Missas")
    yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
    st.link_button("▶️ ASSISTIR AO VIVO NO YOUTUBE", yt_url, use_container_width=True)
    
    st.info("**Horários das Missas:**\n\n- Dom: 08h, 10h e 19h\n- Ter a Sex: 19h")

with col_lit:
    st.subheader("📖 Liturgia Diária")
    hoje = datetime.now().strftime('%d/%m/%Y')
    st.markdown(f"""
