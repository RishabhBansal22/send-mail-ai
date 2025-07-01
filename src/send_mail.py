import smtplib
from email.message import EmailMessage
import mimetypes
import os
from dotenv import load_dotenv

load_dotenv()

class SendMail:
    """Handles email creation and sending."""

    Email_send_schema = {
        "name": "mail_client",
        "description": "send email to the reciever",
        "parameters": {
            "type": "object",
            "properties": {
                "sender_mail": {"type": "string", "description": "email address of sender"},
                "reciever_mail": {"type": "string", "description": "email address of reciever"},
                "subject": {"type": "string", "description": "subject of the email"},
                "content": {"type": "string", "description": "body of the email"},
                "attachment": {"type": "string", "description": "path to attachment"}
            },
            "required": ["reciever_mail", "subject", "content"],
        },
    }

    def __init__(self, sender_mail, reciever_mail, subject, content, attachment=None):
        self.sender_mail = sender_mail
        self.reciever_mail = reciever_mail
        self.subject = subject
        self.content = content
        self.attachment = attachment

    def build_message(self):
        msg = EmailMessage()
        msg["Subject"] = self.subject
        if self.sender_mail:
            msg["From"] = self.sender_mail
        else:
            msg["From"] = os.getenv("default_email")

        msg["To"] = self.reciever_mail
        msg.set_content(self.content)

        if self.attachment:
            with open(self.attachment, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(self.attachment)
                mime_type, _ = mimetypes.guess_type(self.attachment)
                maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)
        return msg

    def send(self):
        try:
            login_email = self.sender_mail if self.sender_mail else os.getenv("default_email")
            with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
                smtp.login(user=login_email, password=os.getenv("gmail_app_pass"))
                smtp.send_message(self.build_message())
            return True  # Email sent successfully
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False