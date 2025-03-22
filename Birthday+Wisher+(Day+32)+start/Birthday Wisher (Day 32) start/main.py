"""import smtplib
password1="yfpvovfkwpjzjyal"
my_email = "pkanth769@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com",465 )

connection.starttls()
connection.login(user=my_email, password=password1)
connection.send_message(from_addr=my_email, to_addrs="pknath761@gmail.com" , msg="Hello")
connection.close()"""
import smtplib

sender = "Private Person <mailtrap@demomailtrap.com>"
receiver = "A Test User <pknath769@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "********69bb")
    server.sendmail(sender, receiver, message)