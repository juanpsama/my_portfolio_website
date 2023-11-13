import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient@example.com"
subject = "Subject of your email"
body = "Body of your email"

# Create the MIME object
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