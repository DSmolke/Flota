from dataclasses import dataclass


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
