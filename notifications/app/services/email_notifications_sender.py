from dataclasses import dataclass
from datetime import date

from flask_mail import Mail

from app.models.dto import EmailNotificationDTO


@dataclass
class EmailNotificationsSender:
    """
    Class used to send email notifications for ending liability of cars.

    :param sending_service: The mailing service used to send emails.
    :type sending_service: Mail
    :param notifications: A list of email notification data transfer objects.
    :type notifications: list[EmailNotificationDTO]
    """
    sending_service: Mail
    notifications: list[EmailNotificationDTO]

    def send_all(self) -> None:
        """
        Sends all notifications stored in the `self.notifications` list.

        :return: None
        """
        for notification in self.notifications:
            days_left = (date.fromisoformat(notification.end_date) - date.today()).days
            self.sending_service.send_email(
                notification.email,
                f"{notification.car_registration} ENDING LIABILITY IN {days_left} DAYS ",
                f"""
                    <html>
                        <body>
                            Hi {notification.first_name}! Car {notification.car_registration} {notification.type} ends within {days_left} days!
                        </body>
                    </html>
                """)