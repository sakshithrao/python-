import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
print("EMAIL:", EMAIL)
print("PASSWORD:", PASSWORD)

def send_email(receiver_email, subject, message):
    try:
        email = EmailMessage()

        email["From"] = EMAIL
        email["To"] = receiver_email
        email["Subject"] = subject

        email.set_content(message)

        # Connect to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(email)

        return "✅ Email sent successfully!"

    except Exception as e:
        return f"❌ Failed to send email.\nError: {e}"