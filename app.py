import streamlit as st

# 1. Configuração
st.set_page_config(page_title="Paróquia N. Sra. Aparecida", page_icon="⛪")

# 2. Títulos
st.title("⛪ Paróquia Nossa Senhora Aparecida")
st.markdown("#### *Caminhando com fé sob o manto de Maria*")
st.divider()

# 3. Transmissões (Links curtos para evitar erro)
st.error("🔴 **ACOMPANHE AS MISSAS AO VIVO**")

yt_link = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
fb_link = "https://facebook.com"

c1, c2 = st.columns(2)
with c1:
    st.link_button("▶️ YOUTUBE (AO VIVO)", yt_link, use_container_width=True)
with c2:
    st.link_button("🔵 FACEBOOK", fb_link, use_container_width=True)

st.divider()

# 4. Horários e Contato
c3, c4 = st.columns(2)
with c3:
    st.markdown("### 🕒 Horários")
    st.write("- **Missas:** Dom 8h, 10h e 19h")
    st.write("- **Semana:** Terça a Sexta 19h")
with c4:
    st.markdown("### 📱 Secretaria")
    st.write("Dúvidas e Batismos:")
    st.link_button("💬 WHATSAPP", "https://wa.me/5511999999999", use_container_width=True)

st.divider()

# 5. Dízimo (Linha encurtada para não cortar)
st.markdown("### 💝 Dízimo e Ofertas")
pix_chave = "12.345.678/0001-99"
st.warning(f"PIX (CNPJ): {pix_chave}")
