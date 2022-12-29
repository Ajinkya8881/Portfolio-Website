import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ajinkya kolhe")
    content = """
   Hi, I am Ajinkya! I am a python programmer, Guitarist and a Gymfreak who loves Photoshoots! I graduated in 2020 with a Bachelor of Engineering degree from Savitri Bai Phule University Pune. here I am showcasing some cool Web apps and Desktop apps which I am building while learning python. Thanks!!!
    """
    st.info(content)
