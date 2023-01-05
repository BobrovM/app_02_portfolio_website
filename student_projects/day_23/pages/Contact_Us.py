import streamlit as st
import sp_send_email as sp_se


st.title("CONTACT US")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox(
        "Topic",
        ("Job Inquiries", "Project Proposals", "Other")
    )
    user_message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        message = f"""\
Subject: business mail from {user_email}

From: {user_email}
Topic: {user_topic}
Message: {user_message}
"""

        sp_se.send_email(message)
        st.info("Your email sent successfully")
