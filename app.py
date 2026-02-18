import streamlit as st
import datetime

# --- CONFIGURAÇÃO DE ALTA PATENTE ---
st.set_page_config(page_title="Portal Paroquial", page_icon="⛪", layout="wide")

# --- DESIGN SYSTEM (CSS MINIMALISTA E ELITISTA) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { background-color: #ffffff; }
    
    .header-box {
        background-color: #002d5b; padding: 50px; border-radius: 20px;
        text-align: center; color: #FFD700; margin-bottom: 30px;
    }
    .header-box h1 { font-family: 'Cinzel', serif; font-size: 3rem !important; margin: 0; }
    
    .section-title {
        font-family: 'Cinzel', serif; color: #002d5b;
        border-bottom: 2px solid #FFD700; padding-bottom: 10px; margin-top: 40px;
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 20px; border-bottom: 1px solid #eee; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; background-color: #f8f9fa; border-radius: 10px 10px 0 0;
        font-family: 'Montserrat', sans-serif; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("""
<div class="header-box">
    <h1>PARÓQUIA NOSSA SENHORA APARECIDA</h1>
    <p style="color:white; font-family:'Montserrat'; letter-spacing: 2px;">COMUNIDADE • FÉ • TRADIÇÃO</p>
</div>
""", unsafe_allow_html=True)

# --- DESTAQUE: CELEBRAÇÃO VIVA ---
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("<h2 class='section-title'>📺 Transmissão ao Vivo</h2>", unsafe_allow_html=True)
    st.write("##")
    yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
    st.link_button("✨ ACESSAR CANAL DE LIVES", yt_url, use_container_width=True)
    st.caption("Acompanhe a Santa Missa em alta definição todos os domingos.")

with col2:
    st.markdown("<h2 class='section-title'>📖 Liturgia Diária</h2>", unsafe_allow_html=True)
    st.write("##")
    hoje = datetime.date.today().strftime('%d de Outubro, %Y') # Exemplo estético
    st.markdown(f"**DATA:** {hoje}")
    st.success("🟢 **TEMPO:** Comum (Semanas da Esperança)")
    st.info("📖 **EVANGELHO:** Meditação Diária no Coração da Igreja")

# --- PORTAL INSTITUCIONAL (OS TÓPICOS) ---
st.markdown("<h2 class='section-title'>🏛️ Portal da Comunidade</h2>", unsafe_allow_html=True)

abas = ["SACRAMENTOS", "PASTORAIS", "AGENDA", "DÍZIMO", "SECRETARIA"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(abas)

with tab1:
    st.write("### Vida Sacramental")
    st.markdown("* **Batismo:** Vida Nova em Cristo.\n* **Eucaristia:** O Pão da Vida.\n* **Matrimônio:** Aliança de Amor.")

with tab2:
    st.write("### Pastorais Ativas")
    col_p1, col_p2 = st.columns(2)
    col_p1.write("- Pastoral da Catequese\n- Vicentinos\n- Coroinhas")
    col_p2.write("- Terço dos Homens\n- Ministério de Música\n- RCC")

with tab3:
    st.write("### Agenda Paroquial")
