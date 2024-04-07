import httpx

from collections import defaultdict
from typing import Any
from datetime import date, timedelta

from flask import Flask

from app.models.mapers import NotificationMapper
from app.parsers.request_json_parser import RequestJsonParser
from app.services.email_notifications_sender import EmailNotificationsSender
from app.email.configuration import MAIL_SETTINGS, MailSender

app = Flask(__name__)


def main():
    with app.app_context():
        # ----------------------------------------------------------------------
        # EMAIL CONFIGURATION
        # ----------------------------------------------------------------------
        app.config.update(MAIL_SETTINGS)
        MailSender.init(app)

        @app.route('/notify-ending-mots-or-insurances/<int:days>')
        def send_mot_insurance_notifications_within_days(days: int):
            """
            Sends MOT and insurance notifications for cars with end dates within a given number of days.

            :param days: The number of days to check for upcoming end dates.
            :return: A dictionary with a success message and status code.
            """
            def with_end_date_within(days_left: int, liability_elements: list[dict[str, Any]]) -> list[dict[str, Any]]:
                return [liability for liability in liability_elements if
                        date.today() <= date.fromisoformat(liability['end_date']) <= date.today() + timedelta(
                            days=days_left)]

            mots = with_end_date_within(
                days,
                RequestJsonParser("http://mots-service:8002/mots/all", "all_mots").parse(httpx)
            )
            insurances = with_end_date_within(
                days,
                RequestJsonParser("http://insurances-service:8004/insurances/all", "all_insurances").parse(
                    httpx)
            )

            drivers = RequestJsonParser("http://drivers:8008/drivers/all", "all_drivers").parse(httpx)

            drivers_by_registration = defaultdict(list)
            for driver in drivers:
                drivers_by_registration[driver['car_registration']].append(driver)

            mots_by_registration = defaultdict(list)
            for mot in mots:
                mots_by_registration[mot['car_registration_number']].append(mot)

            insurances_by_registration = defaultdict(list)
            for insurance in insurances:
                insurances_by_registration[insurance['car_registration_number']].append(insurance)

            notifications = NotificationMapper(mots_by_registration, insurances_by_registration,
                                               drivers_by_registration).map_to_dto_list()

            email_sender = EmailNotificationsSender(MailSender, notifications)
            email_sender.send_all()

            return {'message': 'Notifications sent'}, 200

    return app
