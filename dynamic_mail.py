import os
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

mapping = {
    "edd7fc95-2cd3-4b01-8b65-eca88caf3f8c": os.getenv("MAIL_PASS_HAWI")
}


def send_dynamic_email(sender_email, sender_name, sender_password, recipient_email, subject, body="", html=""):
    """Dynamically configure Flask-Mail for each request"""

    print(sender_name)
    # print("sender email:", sender_email)
    # print("sender name", sender_name)
    # print("sender password", sender_password)
    # print("recipient email", recipient_email)
    # print("subject", subject)
    # print("body", body)
    # print("html", len(html))
    
    # Create a new Flask instance (isolating config)
    app_mail = Flask(__name__)

    # Dynamically set SMTP credentials
    app_mail.config.update(
        {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 587,
            "MAIL_USE_TLS": True,
            "MAIL_USERNAME": sender_email,
            "MAIL_PASSWORD": sender_password,
            "MAIL_DEFAULT_SENDER": (f'{sender_name}', sender_email),
            "MAIL_MAX_EMAILS": None
        }
    )
    

    # Initialize Flask-Mail instance for this request
    mail = Mail(app_mail)

   

    # Create an email message
    
    
    
    # Send the email
    with app_mail.app_context():  # Ensure the new Flask instance has context
        try:
            msg = Message(
                subject=subject,
                # sender=sender_email,
                recipients=[recipient_email],
            )

            if body:
                msg.body = body
            if html:
                msg.html = html
            mail.send(msg)
            
            return {"message": "Email sent successfully!", "from": sender_email}
        except Exception as e:
            return {"error": str(e)}
