import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "aj.kolhe9657@gmail.com"
password = "pbknnbrpibrmpkrc"

receiver = "aj.kolhe8445@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
bye!
"""

with smtplib.SMTP_SSL(host, port, context=context)  as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

