import requests
import smtplib
from email.mime.text import MIMEText

api_key = "76ecba6c3a24712cfb2fb5006d51b893"
OWM_endpoint= "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat":22.572645,
    "lon":88.363892,
    "appid": api_key,
    "cnt":4,

}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather =  response.json()
#print(weather["list"][0]["weather"][0]["id"])
is_true = False
for data in weather["list"]:
    if weather["list"][0]["weather"][0]["id"]:
        is_true=True
if is_true:
    print("It will rain in the next 12 hours")        


# Email details
sender_email = "pknath759@gmail.com"
receiver_email = "pknath761@gmail.com"
subject = "Rain Reminder"
body = "It will rain in 12 Hours"
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server (e.g., Gmail's is smtp.gmail.com)
port = 587  # For TLS
password = "cvfi tjim wbse frpy"  # Replace with your email account password

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Sending the email
try:
    # Set up the server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection with TLS
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()
