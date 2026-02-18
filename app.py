import streamlit as st

# 1. Configuração de Alta Performance
st.set_page_config(page_title="Paróquia N. Sra. Aparecida", page_icon="⛪", layout="wide")

# 2. Design de Elite (CSS Fracionado para evitar erros)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    
    /* Fundo e Fontes */
    .main { background: #fdfdfd; }
    h1 { font-family: 'Playfair Display', serif; color: #002d5b; font-size: 3.5rem !important; text-align: center; }
    
    /* Banner Superior */
    .hero-banner {
        background: linear-gradient(135deg, #002d5b 0%, #0056b3 100%);
        color: #FFD700; padding: 40px; border-radius: 20px;
        text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    /* Cards Profissionais */
    .stButton>button {
        background: white; color: #002d5b; border: 1px solid #e0e0e0;
        border-radius: 12px; height: 100px; font-weight: bold;
        transition: all 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .stButton>button:hover {
        background: #002d5b !important; color: white !important;
        transform: translateY(-5px); border: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. Cabeçalho de Impacto
st.markdown('<div class="hero-banner"><h1>Paróquia Nossa Senhora Aparecida</h1><p style="color:white; font-size:1.2rem;">Portal da Comunidade • Fé e Evangelização</p></div>', unsafe_allow_html=True)

st.write("##")

# 4. Transmissões (Área de Destaque)
st.markdown("### 🎥 Celebrações Ao Vivo")
yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
fb_url = "https://facebook.com"

col1, col2 = st.columns(2)
with col1:
    st.link_button("📺 ASSISTIR NO YOUTUBE", yt_url, use_container_width=True)
with col2:
    st.link_button("👥 COMUNIDADE NO FACEBOOK", fb_url, use_container_width=True)

st.write("##")

# 5. Informações e Dízimo (Layout em Grade)
tab1, tab2, tab3 = st.tabs(["🕒 HORÁRIOS", "💝 DÍZIMO", "📱 CONTATO"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Missas Domingo", "08h | 10h | 19h")
    c2.metric("Missas Semana", "Terça a Sexta", "19:00")
    c3.metric("Confissões", "Quinta-feira", "15:00")

with tab2:
    st.markdown("""
    <div style="background:#eef5ff; padding:30px; border-radius:15px; border-left:8px solid #002d5b;">
        <h3 style="color:#002d5b; margin-top:0;">Seja um Dizimista</h3>
        <p>Sua oferta sustenta nossas obras. Contribua via <b>PIX (CNPJ)</b>:</p>
        <code style="font-size:1.5rem; color:#d63384;">12.345.678/0001-99</code>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.write("Precisa de informações sobre Batismo ou Casamento?")
    st.link_button("💬 FALAR COM A SECRETARIA (WHATSAPP)", "https://wa.me/5511999999999", use_container_width=True)

# 6. Rodapé Minimalista
st.markdown("---")
st.markdown("<p style='text-align:center; color:#999;'>© 2026 Paróquia N. Sra. Aparecida | Todos os direitos reservados</p>", unsafe_allow_html=True)
