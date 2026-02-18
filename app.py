import streamlit as st
from datetime import datetime

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(
    page_title="Portal Paroquial | N. Sra. Aparecida",
    page_icon="⛪",
    layout="wide"
)

# 2. DESIGN SYSTEM (CSS DE AGÊNCIA)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    .main { background: #fdfdfd; }
    
    /* Header Profissional */
    .hero-box {
        background: linear-gradient(rgba(0,45,91,0.85), rgba(0,45,91,0.85)), 
                    url('https://images.unsplash.com/photo-1548625149-fc4a29cf7092?q=80&w=1500');
        background-size: cover; background-position: center;
        padding: 100px 20px; text-align: center; color: white;
        border-radius: 0 0 80px 80px; box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    .hero-box h1 { font-family: 'Cinzel', serif; font-size: 4rem !important; color: #FFD700 !important; }
    
    /* Cards de Seção */
    .feature-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-left: 6px solid #002d5b;
        transition: 0.4s ease; height: 100%;
    }
    .feature-card:hover { transform: translateY(-10px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }

    /* Estilo do Calendário Litúrgico */
    .liturgia-box {
        background: #fff9e6; padding: 20px; border-radius: 15px;
        border: 1px solid #ffe4b3; border-top: 5px solid #FFD700;
    }

    /* Botões Customizados */
    .stLinkButton > a {
        background: #002d5b !important; color: white !important;
        border-radius: 8px !important; padding: 15px !important;
        font-weight: 700 !important; width: 100%; display: block; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER (BANNER DE IMPACTO)
st.markdown("""
<div class="hero-box">
    <h1>PARÓQUIA NOSSA SENHORA APARECIDA</h1>
    <p style="font-family:'Montserrat'; font-size:1.4rem; font-weight:300;">
        "Onde a comunidade se encontra com o sagrado"
    </p>
</div>
""", unsafe_allow_html=True)

st.write("##")

# 4. ÁREA PRINCIPAL: LITURGIA E TRANSMISSÕES
col_lit, col_live = st.columns([1, 1.5])

with col_lit:
    st.markdown("### 📖 Calendário Litúrgico")
    with st.container():
        st.markdown(f"""
        <div class="liturgia-box">
            <h4 style="color:#002d5b; margin-top:0;">{datetime.now().strftime('%d/%m/%Y')}</h4>
            <p style="color:#b8860b; font-weight:bold;">Tempo Comum - Ano Litúrgico C</p>
            <p><i>"A tua palavra é lâmpada para os meus pés e luz para o meu caminho." (Salmo 119)</i></p>
            <hr>
            <p><b>1ª Leitura:</b> Atos dos Apóstolos</p>
            <p><b>Evangelho:</b> Segundo Lucas</p>
        </div>
        """, unsafe_allow_html=True)

with col_live:
    st.markdown("### 🎥 Transmissão Ao Vivo")
    yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
    st.image("https://img.youtube.com/vi/Sua_Live_ID/maxresdefault.jpg", caption="Assista à Santa Missa Dominical", use_container_width=True)
    st.link_button("▶️ ACESSAR CANAL DE TRANSMISSÕES", yt_url)

st.write("---")

# 5. TOPICOS: PASTORAIS, SACRAMENTOS E EVENTOS
st.markdown("<h2 style='text-align:center; color:#002d5b;'>Serviços e Comunidade</h2>", unsafe_allow_html=True)
t1, t2, t3, t4 = st.columns(4)

with t1:
    st.markdown("""<div class="feature-card">
        <h4>🕊️ Sacramentos</h4>
        <p>Orientações para Batismo, Crisma, Matrimônio e Unção dos Enfermos.</p>
        <p style="color:#002d5b; font-weight:bold;">Saiba mais -></p>
    </div>""", unsafe_allow_html=True)

with t2:
    st.markdown("""<div class="feature-card">
        <h4>👥 Pastorais</h4>
