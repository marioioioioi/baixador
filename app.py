import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="Paróquia N. Sra. Aparecida", page_icon="⛪")

# 2. Cabeçalho Principal
st.title("⛪ Paróquia Nossa Senhora Aparecida")
st.markdown("#### *'Aonde quer que eu vá, serei guiado pelo Teu manto.'*")

st.divider()

# 3. SEÇÃO DE TRANSMISSÕES (Link Direto para Lives)
st.error("🔴 **ACOMPANHE AS TRANSMISSÕES AO VIVO**")

# Link atualizado para a aba de "Ao Vivo"
link_streams = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"

col_yt, col_fb = st.columns(2)
with col_yt:
    st.link_button("▶️ ASSISTIR NO YOUTUBE (AO VIVO)", link_streams, use_container_width=True)
with col_fb:
    st.link_button("🔵 ASSISTIR NO FACEBOOK", "https://facebook.com", use_container_width=True)

st.divider()

# 4. Informações e Contato
col_missa, col_zap = st.columns(2)

with col_missa:
    st.markdown("### 🕒 Horários de Missa")
    st.write("- **Domingos:** 08h, 10h e 19h")
    st.write("- **Terça a Sexta:** 19h")
    st.info("🙏 **Confissões:** Quintas-feiras às 15h")

with col_zap:
    st.markdown("### 📱 Secretaria Virtual")
    st.write("Dúvidas sobre Batismo, Casamento ou Intenções:")
    # Substitua o número abaixo quando tiver o oficial
    st.link_button("💬 CHAMAR NO WHATSAPP", "https://wa.me/5511999999999", use_container_width=True)

st.divider()

# 5. Dízimo e Ofertas
st.markdown("### 💝 Dízimo e Solidariedade")
st.warning("Sua contribuição sustenta nossas obras evangelizadoras e sociais.")
st.code("Chave PIX (CNPJ): 12.345.678
