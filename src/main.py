import streamlit as st
from config import Streamlit_config

st.set_page_config(**Streamlit_config.page_config)
st.markdown(Streamlit_config.CSS, unsafe_allow_html=True)

st.markdown('<p class="first_titre">SwarmBot Simulator</p>', unsafe_allow_html=True)
