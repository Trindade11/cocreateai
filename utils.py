# utils.py
import streamlit as st
from streamlit_option_menu import option_menu

def load_css():
    # Ajusta o espaçamento no topo
    st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

def display_logo():
    # Exibe a imagem da logo no topo da página
    st.image(r"C:\Users\rodrigo.trindade\Desktop\AI\logo.jpg", width=100)

def sidebar_menu():
    # Estilos personalizados para o menu lateral
    menu_styles = {
        "container": {"padding": "0!important", "background-color": "#f0f0f0"},
        "icon": {"color": "black", "font-size": "16px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "5px",
            "color": "black",
            "background-color": "#f0f0f0",
            "border-radius": "40px",
        },
        "nav-link-selected": {
            "background-color": "#AED6F0",
            "color": "black",
            "font-weight": "bold",
        },
    }

    # Criação do menu lateral utilizando o streamlit_option_menu na barra lateral
    with st.sidebar:
        selected = option_menu(
            menu_title="",  # Título do menu
            options=["Principal", "Contato"],  # Opções do menu
            icons=["house", "envelope"],  # Ícones correspondentes
            menu_icon="",  # Ícone do menu
            default_index=0,  # Índice padrão (começa em 0)
            styles=menu_styles,  # Aplicação dos estilos personalizados
        )
    return selected

