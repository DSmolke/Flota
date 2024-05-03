from django.core.mail import EmailMessage
from django.conf import settings

def send_email(email: str, subject: str, body: str, content_subtype: str = 'html') -> None:
    email_message = EmailMessage(subject, body, to=[email])
    email_message.content_subtype = content_subtype
    email_message.send()
