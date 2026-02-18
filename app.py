import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida | Oficial",
    page_icon="⛪",
    layout="wide"
)

# --- ESTILO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap');

    .main { background-color: #f8f9fa; }
    
    .titulo-principal {
        font-family: 'Playfair Display', serif;
        color: #002d5b;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0px;
    }

    .subtitulo {
        font-family: 'Roboto', sans-serif;
        color: #666;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }

    /* Banner de Transmissão */
    .live-container {
        background: linear-gradient(135deg, #002d5b 0%, #0056b3 100%);
        color: white;
        padding: 40px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        margin-bottom: 40px;
    }

    .btn-live {
        display: inline-block;
        padding: 15px 30px;
        margin: 10px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        transition: transform 0.3s;
        color: white !important;
    }

    .btn-live:hover { transform: scale(1.05); }
    .yt { background-color: #e62117; }
    .fb { background-color: #3b5998; }

    /* Estilo das Abas */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f1f1;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<h1 class="titulo-principal">Paróquia Nossa Senhora Aparecida</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Comunidade de fé sob o manto da Rainha e Padroeira do Brasil</p>', unsafe_allow_html=True)

# --- SEÇÃO DE TRANSMISSÃO AO VIVO ---
st.markdown("""
    <div class="live-container">
        <h2 style="color: white; border: none;">🎥 Transmissões ao Vivo</h2>
        <p style="color: #e0e0e0; font-size: 1.2rem;">Acompanhe a Santa Missa em tempo real pelos nossos canais oficiais</p>
        <a href="https://www.youtube.com/@SuaParoquia" class="btn-live yt">🔴 Assistir no YouTube</a>
        <a href="https://www.facebook.com/SuaParoquia" class="btn-live fb">🔵 Assistir no Facebook</a>
    </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 A Paróquia", "🕒 Horários", "🙏 Intenções", "💝 Dízimo"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://
