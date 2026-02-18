import streamlit as st

# 1. Configuração Inicial
st.set_page_config(page_title="Paróquia Oficial", page_icon="⛪", layout="wide")

# 2. Estilo Visual (CSS) - Fechado corretamente
st.markdown("""
<style>
    .main { background-color: #ffffff; }
    .hero {
        background: linear-gradient(rgba(0,45,91,0.7), rgba(0,45,91,0.7)), url('https://images.unsplash.com/photo-1548625149-fc4a29cf7092?q=80&w=1000');
        background-size: cover; padding: 60px; text-align: center; color: white; border-radius: 0 0 30px 30px;
    }
    .card {
        background: #f8f9fa; border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-top: 5px solid #002d5b; margin-bottom: 20px;
    }
    .btn {
        display: inline-block; padding: 10px 20px; border-radius: 20px; 
        text-decoration: none; font-weight: bold; color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Banner Principal
st.markdown('<div class="hero"><h1>Paróquia Nossa Senhora Aparecida</h1><p>Mãe Aparecida, rogai por nós!</p></div>', unsafe_allow_html=True)

st.write("---")

# 4. Links de Transmissão e Redes (Sem colunas complexas para evitar erro de indentação)
st.markdown("### 🎥 Transmissões e Contato")

# Cartão YouTube
st.markdown("""
<div class="card">
    <h3 style="color:#FF0000">YouTube Oficial</h3>
    <p>Assista às Missas ao Vivo todos os Domingos</p>
    <a href="https://youtube.com" class="btn" style="background:#FF0000">ABRIR YOUTUBE</a>
</div>
""", unsafe_allow_html=True)

# Cartão Facebook
st.markdown("""
<div class="card">
    <h3 style="color:#187
