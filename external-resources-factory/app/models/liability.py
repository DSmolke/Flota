from dataclasses import dataclass
from typing import Any, Self
from app.models.model_interface import ModelInterface


@dataclass(frozen=True)
class Liability(ModelInterface):
    """

    The `Liability` class represents a liability related to a car insurance policy or car mot policy.

    Attributes:
        legal_identifier (str): The legal identifier of the liability.
        start_date (str): The start date of the liability.
        end_date (str): The end date of the liability.
        car_registration_number (str): The registration number of the car associated with the liability.
        active (str): The status of the liability (active or inactive).

    Methods:
        from_dict(data: dict[str, Any]) -> Liability:
            This class method creates a new `Liability` instance from a dictionary containing the liability data.

        as_dict() -> dict[str, Any]:
            This method returns the liability data as a dictionary.

    """
    legal_identifier: str
    start_date: str
    end_date: str
    car_registration_number: str
    active: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """

            from_dict(data: dict[str, Any]) -> Self

            Construct a new instance of the class using a dictionary.

            Args:
                data (dict): A dictionary containing the data needed to construct the instance.

            Returns:
                Self: A new instance of the class.

        """
        return cls(
            legal_identifier=data["legal_identifier"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            car_registration_number=data["car_registration_number"],
            active=data["active"]
        )

    def as_dict(self) -> dict[str, Any]:
        """
        Convert the object to a dictionary.

        Returns:
            A dictionary representation of the object with the following keys:
                - 'legal_identifier' (str): The legal identifier of the object.
                - 'start_date' (datetime): The start date of the object.
                - 'end_date' (datetime): The end date of the object.
                - 'car_registration_number' (str): The car registration number associated with the object.
                - 'active' (bool): The active status of the object.

        """
        return {
            "legal_identifier": self.legal_identifier,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "car_registration_number": self.car_registration_number,
            "active": self.active
        }
