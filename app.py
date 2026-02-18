import streamlit as st
import datetime

# 1. SETUP
st.set_page_config(page_title="Paróquia", layout="wide")

# 2. HEADER
st.title("⛪ Paróquia N. Sra. Aparecida")
st.write("Portal Oficial da Comunidade")
st.divider()

# 3. LINKS LIVES
st.subheader("🔴 Transmissões")
yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
st.link_button("ASSISTIR NO YOUTUBE", yt_url)

st.divider()

# 4. CALENDARIO
st.subheader("📖 Liturgia")
hoje = datetime.date.today().strftime('%d/%m/%Y')
st.info(f"Data: {hoje} | Tempo: Comum")

st.divider()

# 5. TOPICOS (ABAS)
st.subheader("🏛️ Informações")
aba1, aba2, aba3 = st.tabs(["MISSA", "DIZIMO", "CONTATO"])

with aba1:
    st.write("**Domingo:** 08h, 10h, 19h")
    st.write("**Semana:** 19h")

with aba2:
    st.write("**PIX CNPJ:**")
    st.code("12.345.678/0001-99")

with aba3:
    st.write("**Secretaria:**")
    st.write("Seg a Sex: 08h às 17h")
    st.link_button("WHATSAPP", "https://wa.me/5511999999999")

st.divider()

# 6. RODAPE
st.caption("© 2026 Paróquia Oficial")
