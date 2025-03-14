import streamlit as st

st.title("🎈 Techschool 2025 Tutorial Streamlit na cloud")
st.header("Primeiro cabeçalho")
st.subheader("Meninas apaixonadas por tecnologia aprendendo a programar")
st.write(
    "Primeiro tutorial da Techschool 2025 com Streamlit"
)
st.markdown (
        """
        <style>
            .stApp{
                 background-color: #E0F8EC; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )
st.set_page_config(page_title="Corpo Humano", layout="centered")


st.markdown(
    """
    <style>
        .title {font-size: 28px;font-weight: bold;text-align: center;
        color: #6D3B2C;background-color: #D4C2A8;padding: 10px;border-radius: 10px;   
        width: 80%;margin: auto;
        }
        .circle-button {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: #A3D39C;
            color: black;
            font-size: 18px;
            font-weight: bold;
            margin: 10px;
            cursor: pointer;
            text-align: center;
            line-height: 100px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .bottom-menu {
            display: flex;
            justify-content: space-around;
            padding: 15px;
            background-color: #6D3B2C;
            border-radius: 10px;
            position: fixed;
            bottom: 10px;
            width: 90%;
            left: 5%;
            color: white;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título
st.markdown('<div class="title">🌞 Corpo Humano</div>', unsafe_allow_html=True)

# Ícones interativos
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Criação de botões simulando os círculos
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(":sun_with_face:"):
        st.success("Você selecionou: Áudio")

with col2:
    if st.button(":book:"):
        st.success("Você selecionou: Livro")

with col3:
    if st.button(":loudspeaker:"):
        st.success("Você selecionou: Som")

col4, col5 = st.columns(2)

with col4:
    if st.button("🏆"):
        st.success("Você selecionou: Desafios")

st.markdown('</div>', unsafe_allow_html=True)

# Barra de navegação inferior
st.markdown(
    """
    <div class="bottom-menu">
        🏠 menu | 🌳 | 👧🏽
    </div>
    """,
    unsafe_allow_html=True,
)
