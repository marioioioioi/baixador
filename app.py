import streamlit as st
from datetime import datetime

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Portal Paroquial N. Sra. Aparecida", page_icon="⛪", layout="wide")

# 2. CSS DE ALTA PERFORMANCE (FECHADO CORRETAMENTE)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    .main { background-color: #f4f7f9; }
    .hero-bg {
        background: linear-gradient(135deg, #002d5b 0%, #004a8d 100%);
        color: #FFD700; padding: 60px; border-radius: 25px; text-align: center;
        margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .hero-bg h1 { font-family: 'Cinzel', serif; font-size: 3.5rem !important; }
    .liturgia-card {
        background: white; border-left: 8px solid #FFD700;
        padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: white; border-radius: 10px; padding: 10px 20px; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO (BANNER HERO)
st.markdown("""
<div class="hero-bg">
    <h1>PARÓQUIA NOSSA SENHORA APARECIDA</h1>
    <p style="color:white; font-family:'Montserrat'; font-size:1.2rem;">Portal da Fé e Comunidade Paroquial</p>
</div>
""", unsafe_allow_html=True)

# 4. CALENDÁRIO LITÚRGICO E TRANSMISSÕES
col_lit, col_live = st.columns([1, 1.3])

with col_lit:
    st.markdown
