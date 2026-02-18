import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida | Links Oficiais",
    page_icon="⛪",
    layout="centered"
)

# --- ESTILO CSS PARA BOTÕES PROFISSIONAIS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@400&display=swap');

    .main { background-color: #f4f7f9; }
    
    .header-container {
        text-align: center;
        padding: 20px;
        margin-bottom: 30px;
    }

    .igreja-nome {
        font-family: 'Playfair Display', serif;
        color: #002d5b;
        font-size: 2.5rem;
        margin-bottom: 5px;
    }

    /* Estilo dos Botões de Link */
    .link-button {
        display: block;
        width: 100%;
        background-color: white;
        color: #002d5b !important;
        padding: 18px;
        margin-bottom: 15px;
        text-align: center;
        text-decoration: none;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
        border-radius: 12px;
        border: 1px solid #d1d9e6;
        box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
        transition: all 0.3s ease;
    }

    .link-button:hover {
        transform: translateY(-3px);
        box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
        background-color: #002d5b;
        color: white !important;
    }

    .link-especial {
        background: linear-gradient(135deg, #002d5b 0%, #0056b3 100%);
        color: white !important;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/2881/2881023.png" width="80">
        <h1 class="igreja-nome">Nossa Senhora Aparecida</h1>
        <p style="color: #666;">Paróquia Matriz - Bem-vindo à nossa comunidade</p>
    </div>
    """, unsafe_allow_html=True)

# --- LISTA DE LINKS (SITE POR LINKS) ---

# 1. Transmissão Ao Vivo (Link Especial)
st.markdown('<a href="https://youtube.com" class="link-button link-especial">🎥 ASSISTIR MISSA AO VIVO (YOUTUBE)</a>', unsafe_allow_html=True)

# 2. Facebook
st.markdown('<a href="https://facebook.com" class="link-button">🔵 NOSSO FACEBOOK (FOTOS E AVISOS)</a>', unsafe_allow_html=True)

# 3. WhatsApp da Secretaria
st.markdown('<a href="https://wa.me/5511999999999" class="link-button">📱 WHATSAPP DA SECRETARIA</a>', unsafe_allow_html=True)

# 4. Horários de Missa (Link para um PDF ou Imagem da Agenda)
st.markdown('<a href="#" class="link-button">🕒 CONFIRA NOSSOS HORÁRIOS</a>', unsafe_allow_html=True)

# 5. Intenções de Missa (Link para formulário Google ou WhatsApp)
st.markdown('<a href="#" class="link-button">📝 ENVIAR INTENÇÕES PARA O ALTAR</a>', unsafe_allow_html=True)

# 6. Dízimo e Ofertas (PIX)
st.markdown('<a href="#" class="link-button">💝 CONTRIBUIR COM O DÍZIMO (PIX)</a>', unsafe_allow_html=True)

# 7. Localização (Google Maps)
st.markdown('<a href="https://maps.google.com" class="link-button">📍 COMO CHEGAR NA MATRIZ</a>', unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown("<br><p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 Paróquia Nossa Senhora Aparecida</p>", unsafe_allow_html=True)
