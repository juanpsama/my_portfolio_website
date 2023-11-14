import smtplib
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')
recipient_email = "samajpablo@gmail.com"

def send_email(name, email, phone, message):
    # Create the MIME object
    print(name)
    print(email)
    print(phone)
    print(message)
    body = f"Nombre:{name} \nEmail: {email} \nPhone:{phone} \nMensaje: {message}"
    print(body)
    subject = "Contact from Portfolio WebSite"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Establish a connection with the SMTP server (in this case, Gmail's SMTP server)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully.")