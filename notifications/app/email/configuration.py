import logging
from flask_mail import Mail, Message

from app.env_variables import MAIL_USERNAME, MAIL_PASSWORD


logger = logging.getLogger(__name__)

MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
}


class MailSender:
    """Class to send emails."""
    mail = None

    @classmethod
    def init(cls, app):
        """
        :param app: Flask application instance
        :return: None

        This method initializes the Mail object for sending emails.

        Example usage:
        ```python
        app = Flask(__name__)
        Mail.init(app)
        ```
        """
        cls.mail = Mail(app)

    @classmethod
    def send_email(cls, email: str, topic: str, html_body: str) -> None:
        """
        Send an email to the specified email address.

        :param email: The recipient's email address.
        :param topic: The subject of the email.
        :param html_body: The HTML body of the email.
        :return: None
        """
        message = Message(
            subject=topic,
            sender='ds.messanger@gmail.com',
            recipients=[email],
            html=html_body
        )

        MailSender.mail.send(message)
