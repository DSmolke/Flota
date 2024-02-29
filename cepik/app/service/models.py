from dataclasses import dataclass
from typing import Any


@dataclass
class CarDetails:
    """
    The `CarDetails` class represents the details of a car.

    Attributes:
        registration (str): The registration number of the car.
        vin (str): The Vehicle Identification Number (VIN) of the car.
        first_registration_date (str): The date of the car's first registration.
    """
    registration: str
    vin: str
    first_registration_date: str

    def as_dict(self) -> dict[str, Any]:
        """
        Converts the object into a dictionary representation.

        :return: A dictionary containing the object's properties.
        :rtype: dict[str, Any]
        """
        return {
            "registration": self.registration,
            "vin": self.vin,
            "first_registration_date": self.first_registration_date
        }
