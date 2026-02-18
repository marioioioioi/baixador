import streamlit as st
import datetime

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Portal Paroquial", page_icon="⛪", layout="wide")

# 2. CABEÇALHO (Simples e Direto)
st.title("⛪ Paróquia Nossa Senhora Aparecida")
st.caption("Portal Oficial da Comunidade - Fé e Evangelização")
st.divider()

# 3. DESTAQUES (YouTube e Liturgia)
col1, col2 = st.columns([1, 1])

with col1:
    st.error("🔴 TRANSMISSÃO AO VIVO")
    yt = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
    st.link_button("▶️ ACESSAR YOUTUBE (LIVES)", yt, use_container_width=True)
    st.info("Missas: Ter a Sex às 19h | Dom às 08h, 10h e 19h")

with col2:
    st.warning("📖 LITURGIA DIÁRIA")
    hoje = datetime.date.today().strftime('%d/%m/%Y')
    st.write(f"📅 **Data:** {hoje}")
    st.write("🟢 **Tempo:** Comum (Ano C)")
    st.write("📖 **Evangelho:** Segundo Lucas")

st.divider()

# 4. PORTAL DE TÓPICOS (O "Mais Profissional")
st.subheader("🏛️ Serviços e Comunidade")
aba1, aba2, aba3, aba4 = st.tabs(["⛪ SACRAMENTOS", "👥 PASTORAIS", "📅 AGENDA", "💝 DÍZIMO"])

with aba1:
    st.markdown("### Orientações Sacramentais")
    st.write("- **Batismo:** Inscrições na secretaria.")
    st.write("- **Matrimônio:** Agendar com 6 meses de antecedência.")
    st.write("- **Confissões:** Quintas-feiras, das 14h às 17h.")

with aba2:
    st.markdown("### Pastorais e Movimentos")
    st.write("- Pastoral da Catequese")
    st.write("- Vicentinos (Assistência Social)")
    st.write("- Terço dos Homens e das Mulheres")
    st.write("- RCC (Grupo de Oração)")

with aba3:
    st.markdown("### Calendário da Paróquia")
    st.write("📅 **Março:** Retiro Espiritual de Quaresma")
    st.write("📅 **Outubro:** Novena e Festa da Padroeira")
    st.write("📅 **Todo 1º Sábado:** Adoração ao Santíssimo às 07h")

with aba4:
    st.markdown("### Oferta de Amor e
