import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida | Oficial",
    page_icon="⛪",
    layout="wide"
)

# --- ESTILO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    /* Importando fonte elegante */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap');

    .main { background-color: #fcfcfc; }
    
    h1 { font-family: 'Playfair Display', serif; color: #002d5b; font-size: 3rem !important; }
    h2, h3 { font-family: 'Playfair Display', serif; color: #004080; }
    p { font-family: 'Roboto', sans-serif; color: #444; }

    /* Estilização dos Cards */
    .st-emotion-cache-1r6slb0 {
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        padding: 20px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* Botões de Redes Sociais */
    .btn-social {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 10px 20px;
        border-radius: 10px;
        text-decoration: none;
        color: white !important;
        font-weight: bold;
        margin: 5px;
    }
    .btn-yt { background-color: #FF0000; }
    .btn-fb { background-color: #1877F2; }
    
    /* Banner de Transmissão */
    .live-banner {
        background: linear-gradient(90deg, #002
