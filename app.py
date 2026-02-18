import streamlit as st

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida | Portal Oficial",
    page_icon="⛪",
    layout="wide"
)

# --- CSS AVANÇADO (DESIGN DE AGÊNCIA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    /* Fundo e Container */
    .main { background-color: #ffffff; }
    
    /* Hero Section (Banner) */
    .hero {
        background: linear-gradient(rgba(0, 45, 91, 0.8), rgba(0, 45, 91, 0.8)), 
                    url('https://images.unsplash.com/photo-1548625149-fc4a29cf7092?q=80&w=2000');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        text-align: center;
        border-radius: 0 0 50px 50px;
        color: white;
        margin-bottom: 40px;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 4rem !important;
        margin-bottom: 10px;
        color: #FFD700 !important; /* Dourado */
    }

    /* Cards de Transmissão */
    .live-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-top: 5px solid #002d5b;
        transition: 0.3s;
    }
    .live-card:hover { transform: translateY(-10px); }

    /* Botões Profissionais */
    .btn-custom {
        display: inline-block;
        padding: 12px 25px;
        margin: 10px;
        border-radius: 30px;
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    .btn-yt { background-color: #FF0000; color: white !important; }
    .btn-fb { background-color: #1877F2; color: white !important; }
    .btn-pix { background-color: #32BCAD; color: white !important; }

    /* Grid de Horários */
    .horario-box {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 15px
