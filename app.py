import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="Paróquia N. Sra. Aparecida", page_icon="⛪")

# 2. Cabeçalho Estilizado
st.title("⛪ Paróquia Nossa Senhora Aparecida")
st.subheader("Bem-vindo à nossa comunidade de fé!")

# 3. Banner de Transmissão (YouTube e Facebook)
st.error("🔴 **TRANSMISSÕES AO VIVO**")
col_yt, col_fb = st.columns(2)
with col_yt:
    st.link_button("▶️ ASSISTIR NO YOUTUBE", "https://youtube.com", use_container_width=True)
with col_fb:
    st.link_button("🔵 ASSISTIR NO FACEBOOK", "https://facebook.com", use_container_width=True)

st.divider()

# 4. Informações Principais
col_info, col_zap = st.columns(2)

with col_info:
    st.markdown("### 🕒 Horários de Missa")
    st.write("- **Domingos:** 08h, 10h e 19h")
    st.write("- **Terça a Sexta:** 19h")
    st.write("- **Confissões:** Quinta às 15h")

with col_zap:
    st.markdown("### 📱 Contato")
    st.write("Fale com a nossa secretaria:")
    st.link_button("💬 CHAMAR NO WHATSAPP", "https://wa.me/5511999999999", use_container_width=True)

st.divider()

# 5. Dízimo e Ofertas
st.markdown("### 💝 Dízimo e Solidariedade")
st.info("Sua generosidade mantém nossa paróquia viva!")
st.code("Chave PIX (CNPJ): 12.345.678/0001-99", language="text")
st.caption("Mitra Diocesana - Paróquia Nossa Senhora Aparecida")

# 6. Localização
st.divider()
st.markdown("### 📍 Localização")
st.link_button("🗺️ VER NO GOOGLE MAPS", "https://goo.gl/maps/exemplo", use_container_width=True)

# 7. Rodapé
st.write("---")
st.caption("© 2026 Paróquia Nossa Senhora Aparecida - Todos os direitos reservados.")
