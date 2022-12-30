import streamlit as st

st.header("Contact Us")

    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message= message + user_email