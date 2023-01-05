import streamlit as st
import send_email as se


st.title("Contact me!")

with st.form(key="email_form"):
    user_email = st.text_input("Your email")
    subject = st.text_input("Subject")
    raw_message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        message = f"""\
Subject: Portfolio email from {user_email} about: {subject}

From: {user_email}

Message: {raw_message}
"""
        se.send_email(message)
        st.info("Your email is sent successfully")
