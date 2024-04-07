from dataclasses import dataclass
from typing import Any

from app.models.dto import EmailNotificationDTO


@dataclass
class NotificationMapper:
    """

    The `NotificationMapper` class is responsible for mapping data from various sources into a list of `EmailNotificationDTO` objects.

    Attributes:
        - mots: A dictionary containing MOT data for each car registration number.
        - insurances: A dictionary containing insurance data for each car registration number.
        - drivers: A dictionary containing driver data for each car registration number.

    Methods:
        - map_to_dto_list(): Maps the data from mots, insurances, and drivers dictionaries into a list of `EmailNotificationDTO` objects. Returns the list of notifications.

    Example Usage:

        mapper = NotificationMapper(mots_data, insurances_data, drivers_data)
        notifications = mapper.map_to_dto_list()

    """
    mots: dict[str, Any]
    insurances: dict[str, Any]
    drivers: dict[str, Any]

    def map_to_dto_list(self) -> list[EmailNotificationDTO]:
        """
        Maps the internal data structure to a list of EmailNotificationDTO objects.

        :return: A list of EmailNotificationDTO objects.
        :rtype: list[EmailNotificationDTO]
        """
        notifications = []
        for car_registration, drivers_list in self.drivers.items():
            mots_for_car = self.mots[car_registration]
            insurances_for_car = self.insurances[car_registration]
            for driver in drivers_list:
                notifications.extend([EmailNotificationDTO('MOT', car_registration, driver['first_name'],
                                                           driver['email'], mot_data['end_date']) for
                                      mot_data in mots_for_car])
                notifications.extend(
                    [EmailNotificationDTO('Insurance', car_registration, driver['first_name'],
                                          driver['email'], insurance_data['end_date']) for insurance_data in
                     insurances_for_car])
        return notifications

