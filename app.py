import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Paróquia Nossa Senhora Aparecida",
    page_icon="⛪",
    layout="centered"
)

# --- ESTILO CUSTOMIZADO (Azul e Dourado) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #003366; color: white; }
    h1 { color: #003366; text-align: center; border-bottom: 2px solid #ffd700; }
    .css-10trblm { color: #003366; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("⛪ Paróquia Nossa Senhora Aparecida")
st.markdown("<p style='text-align: center;'><i>'Aonde quer que eu vá, serei guiado pelo Teu manto.'</i></p>", unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Nossa_Senhora_Aparecida_-_escultura.jpg/250px-Nossa_Senhora_Aparecida_-_escultura.jpg", width=150)
st.sidebar.title("Secretaria Virtual")
opcao = st.sidebar.radio("Navegue pelo site:", 
    ["Início", "Horários de Missa", "Pedidos de Oração", "Dízimo e Ofertas", "Notícias"])

st.sidebar.divider()
st.sidebar.info("📍 Rua da Matriz, 123 - Centro\n\n📞 (11) 99999-9999")

# --- LÓGICA DAS PÁGINAS ---

if opcao == "Início":
    st.image("https://images.unsplash.com/photo-1548625149-fc4a29cf7092?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="Nossa Casa de Oração")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Boas-vindas")
        st.write("""
        Seja bem-vindo ao nosso portal digital! Nossa paróquia é um lugar de acolhida, 
        fé e devoção à nossa Padroeira. Aqui você encontra todas as informações 
        para participar da nossa comunidade.
        """)
    with col2:
        st.subheader("Palavra do Pároco")
        st.info("“A fé não é apenas um sentimento, é uma decisão de caminhar com Cristo.” — Pe. João Silva")

elif opcao == "Horários de Missa":
    st.header("🕒 Horários de Celebrações")
    
    with st.expander("⛪ Missas na Matriz", expanded=True):
        st.write("**Terça a Sexta:** 19h")
        st.write("**Sábado:** 18h")
        st.write("**Domingo:** 08h, 10h e 19h")

    with st.expander("🙏 Confissões"):
        st.write("**Quinta-feira:** 14h às 17h")
        st.write("**Sexta-feira:** 09h às 11h")
    
    with st.expander("📖 Batizados"):
        st.write("Todo 2º domingo do mês, após a missa das 10h. Procure a secretaria com 15 dias de antecedência.")

elif opcao == "Pedidos de Oração":
    st.header("🙏 Pedidos de Oração")
    st.write("Deixe aqui suas intenções para que possamos rezar por você nas missas da semana.")
    
    with st.form("form_oracao"):
        nome = st.text_input("Seu Nome")
        tipo = st.selectbox("Tipo de Intenção", ["Agradecimento", "Saúde", "Falecimento", "Causas Impossíveis"])
        mensagem = st.text_area("Sua intenção")
        submit = st.form_submit_button("Enviar para o Altar")
        
        if submit:
            st.success(f"Obrigado, {nome}. Seu pedido foi enviado e será colocado aos pés de Nossa Senhora.")

elif opcao == "Dízimo e Ofertas":
    st.header("💝 Dízimo e Solidariedade")
    st.write("""
    O dízimo é um ato de gratidão e devolução. Graças à sua generosidade, 
    mantemos nossas obras de caridade e a conservação da nossa igreja.
    """)
    
    st.warning("🔑 **Chave PIX (CNPJ):** 00.000.000/0001-00")
    st.write("**Banco:** Mitra Diocesana")
    
    if st.button("Quero ser dizimista (Cadastrar)"):
        st.text_input("Seu Telefone")
        st.button("Enviar contato")

elif opcao == "Notícias":
    st.header("📰 Mural da Comunidade")
    
    st.markdown("---")
    st.subheader("🍓 Festa da Padroeira 2026")
    st.write("Já começaram os preparativos para a nossa quermesse! Venha ser voluntário nas barracas.")
    
    st.markdown("---")
    st.subheader("🎨 Catequese 2026")
    st.write("Inscrições abertas para a Primeira Eucaristia. Traga o registro de batismo da criança.")

# --- RODAPÉ ---
st.divider()
st.markdown("<p style='text-align: center; font-size: 0.8em;'>© 2026 Paróquia Nossa Senhora Aparecida - Desenvolvido com Fé</p>", unsafe_allow_html=True)
