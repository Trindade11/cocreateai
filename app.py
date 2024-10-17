# app.py
import streamlit as st
from utils import load_css, display_logo, sidebar_menu

st.set_page_config(
    page_title="IR",
    page_icon="✔️",
    layout="wide",
    initial_sidebar_state="auto",
)

# Carrega o CSS personalizado e exibe o logo
load_css()
display_logo()

# Exibe o menu lateral e obtém a seleção (certifique-se de que o menu é chamado apenas aqui)
selected = sidebar_menu()

# Navegação entre páginas com base na seleção do menu
if selected == "Principal":
    from modules import principal
    principal.app()
elif selected == "Contato":
    from modules import contato
    contato.app()





