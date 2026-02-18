import streamlit as st

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida | Portal Oficial",
    page_icon="⛪",
    layout="wide"
)

# --- CSS AVANÇADO (DESIGN PROFISSIONAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');

    /* Fundo */
    .main { background-color: #ffffff; }
    
    /* Hero Section (Banner) */
    .hero {
        background: linear-gradient(rgba(0, 45, 91, 0.7), rgba(0, 45, 91, 0.7)), 
                    url('https://images.unsplash.com/photo-1548625149-fc4a29cf7092?q=80&w=2000');
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        text-align: center;
        border-radius: 0 0 40px 40px;
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem !important;
        color: #FFD700 !important;
        margin-bottom: 10px;
    }

    /* Cards de Transmissão */
    .card-premium {
        background: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border-top: 6px solid #002d5b;
        transition: 0.3s ease;
        height: 100%;
    }
    .card-premium:hover { transform: translateY(-5px); }

    /* Botões */
    .btn-link {
        display: inline-block;
        padding: 12px 25px;
        margin-top: 15px;
        border-radius: 30px;
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-weight
