import streamlit as st

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida",
    page_icon="⛪",
    layout="wide"
)

# 2. CSS CUSTOMIZADO (DESIGN DE AGÊNCIA)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');
    
    /* Configurações Gerais */
    .main { background: #fcfcfc; }
    
    /* Banner de Impacto (Hero) */
    .hero-section {
        background: linear-gradient(135deg, #002d5b 0%, #004a8d 100%);
        padding: 60px 20px;
        border-radius: 0 0 50px 50px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 40px;
    }
    
    .hero-section h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem !important;
        color: #FFD700 !important;
        margin-bottom: 5px;
    }

    /* Cartões de Informação */
    .info-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-bottom: 5px solid #FFD700;
        text-align: center;
        transition: 0.3s;
    }
    .info-card:hover { transform: translateY(-10px); }

    /* Estilização de Links/Botões */
    .stLinkButton > a {
        background: #002d5b !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-weight: 700 !important;
        border: none !important;
        transition: 0.4s !important;
        text-decoration: none;
    }
    .stLinkButton > a:hover {
        background: #FFD700 !important;
        color: #002d5b !important;
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER (HERO SECTION)
st.markdown("""
<div class="hero-section">
    <h1>Paróquia Nossa Senhora Aparecida</h1>
    <p style="font-family: 'Montserrat'; font-weight: 300; font-size: 1.2rem;">
        Comunidade de Fé, Esperança e Caridade
    </p>
</div>
""", unsafe_allow_html=True)

# 4. ÁREA DE TRANSMISSÕES (O QUE VOCÊ PEDIU)
st.write("##")
col_yt, col_fb = st.columns(2)

yt_url = "https://www.youtube.com/@paroquianossasenhoraaparec730/streams"
fb_url = "https://www.facebook.com" # Substitua pelo link real

with col_yt:
    st.markdown("""
    <div style="text-align:center;">
        <h3 style="color:#002d5b;">Canais Oficiais</h3>
        <p>Acompanhe a Santa Missa ao vivo e receba bênçãos em sua casa.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("▶️ ASSISTIR NO YOUTUBE", yt_url, use_container_width=True)

with col_fb:
    st.markdown("""
    <div style="text-align:center;">
        <h3 style="color:#002d5b;">Rede Comunitária</h3>
        <p>Participe da nossa comunidade, veja fotos e avisos paroquiais.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🔵 SEGUIR NO FACEBOOK", fb_url, use_container_width=True)

st.write("##")
st.divider()

# 5. INFORMAÇÕES PAROQUIAIS (DESIGN EM GRID)
st.markdown("<h2 style='text-align:center; color:#002d5b;'>Informações Úteis</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <h4>🕒 Missas</h4>
        <p><b>Domingos:</b><br>08h, 10h e 19h</p>
        <p><b>Semana:</b><br>Terça a Sexta às 19h</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <h4>💝 Dízimo</h4>
        <p>Contribua com a evangelização</p>
        <code style="color:#002d5b; font-size:1rem;">12.345.678/0001-99</code>
        <p style="font-size:0.8rem; margin-top:10px;">Chave PIX (CNPJ)</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <h4>📱 Secretaria</h4>
        <p>Batismos e Casamentos</p>
        <p>Fale conosco agora:</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("💬 WHATSAPP", "https://wa.me/5511999999999", use_container_width=True)

# 6. RODAPÉ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:20px; color:#888; font-size:0.9rem; border-top:1px solid #eee;">
    © 2026 Paróquia Nossa Senhora Aparecida | Praça da Matriz, Centro<br>
    <i>"Sob a proteção da Mãe Aparecida"</i>
</div>
""", unsafe_allow_html=True)
