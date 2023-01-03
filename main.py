import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Name Surname")
    content_main_info = """Hi, this is placeholder for my future web portfolio.
    It is empty right now, but i will put more stuff in here later."""
    st.write(content_main_info)

content_intro = """You can find my projects below. Feel free to contact me!"""
st.write(content_intro)