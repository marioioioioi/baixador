import streamlit as st

# Configuração de Elite
st.set_page_config(page_title="Paróquia Oficial", page_icon="⛪", layout="wide")

# CSS Profissional Compacto
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@400;700&display=swap');
    .main { background-color: #ffffff; }
    .hero {
        background: linear-gradient(rgba(0,45,91,0.7), rgba(0,45,91,0.7)), url('https://images.unsplash.com/photo-1548625149-fc4a29cf7092?q=80&w=1000');
        background-size: cover; padding: 60px; text-align: center; border-radius: 0 0 30px 30px; color: white;
    }
    .hero h1 { font-family: 'Playfair Display', serif; color: #FFD700 !important; font-size: 3rem !important; }
    .card {
        background: white; border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #002d5b; transition: 0.3s;
    }
    .card:hover { transform: translateY(-5px); }
    .btn {
        display: inline-block; padding: 10px 20px; border-radius: 20px; text-decoration: none;
        font-weight: bold; color: white !important; margin-top: 10px; font-family: 'Montserrat';
    }
    </style>
    """, unsafe_allow_html=True)

# Banner Principal
st.markdown("""
    <div class="hero">
        <h1>Paróquia Nossa Senhora Aparecida</h1>
        <p style="font-family: 'Montserrat'; font-size: 1.2rem;">"Mãe Aparecida, rogai por nós!"</p>
    </div>
    """, unsafe_allow_html=True)

st.write("##")

# Seção de Transmissões e Links
col1, col2, col3 = st.columns(3)

with col1:
