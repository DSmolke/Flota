from dataclasses import dataclass


@dataclass
class EmailNotificationDTO:
    """
    Data class representing an email notification.

    Attributes:
        type (str): The type of notification (e.g., "reminder", "confirmation").
        car_registration (str): The registration number of the car associated with the notification.
        first_name (str): The first name of the recipient of the email.
        email (str): The email address of the recipient.
        end_date (str): The end date of the notification.

    """
    type: str
    car_registration: str
    first_name: str
    email: str
    end_date: str
