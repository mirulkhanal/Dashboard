import smtplib
from email.message import EmailMessage
from string import Template as tmp
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()  # Loading credentials from the .env file
email_id = os.getenv('EMAIL')
email_to = os.getenv('EMAIL_TO')
password = os.getenv('PASSWORD')
name = os.getenv('USER_NAME')

# Setting email contents
html = tmp(Path("email.html").read_text())
email = EmailMessage()
email['From'] = email_id
email['To'] = email_to
email['Subject'] = 'Testing python Email'

email.set_content(html.substitute(name=name), 'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_id, password)
    smtp.send_message(email)
    print('Successful')
