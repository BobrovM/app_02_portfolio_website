import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "officeguyyt@gmail.com"
    #SMTP_PASSWORD
    password = os.getenv("SMTP_PASSWORD")

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    test_message = """\
Subject: test
email\n
test
    """
    send_email(test_message)
