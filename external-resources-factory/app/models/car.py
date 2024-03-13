from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Self


class CarInterface(ABC):
    """
    CarInterface is an abstract class that defines the interface for a car object.

    Methods:
        - as_dict: Convert the car object to a dictionary.
            Returns:
                dict[str, Any]: The car object as a dictionary.

        - from_dict: Create a car object from a dictionary.
            Parameters:
                data (dict[str, Any]): The dictionary containing the car object data.
            Returns:
                Self: A new car object created from the dictionary.
    """
    @abstractmethod
    def as_dict(self) -> dict[str, Any]:
        """
        Return the object as a dictionary.

        :return: A dictionary containing the attributes of the object.
        :rtype: dict[str, Any]
        """
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """

        Class Method: from_dict

        Description:
        This method is responsible for creating an instance of the current class using the provided dictionary data.

        Parameters:
        - cls: The class object itself.
        - data: A dictionary containing the data necessary to create the instance.

        Returns:
        - The newly created instance.

        Example Usage:
        ```
        data = {
            'attribute_1': value_1,
            'attribute_2': value_2,
        }

        instance = ClassName.from_dict(data)
        ```

        """
        pass


@dataclass
class Car(CarInterface):
    registration: str
    vin: str
    make: str
    model: str
    first_registration_date: str
    production_year: str
    mileage: str
    fuel_consumption: str
    fuel_type_id: int
    vehicle_status_id: int

    def as_dict(self) -> dict[str, Any]:
        """

        Method: as_dict

        This method converts an instance of a class to a dictionary.

        Parameters:
        - self: The instance of the class.

        Return Type:
        - dict[str, Any]: A dictionary representing the instance of the class.

        Example Usage:
            # Create an instance of the class
            car = Car()

            # Convert the instance to a dictionary
            car_dict = car.as_dict()

            # Print the dictionary
            print(car_dict)

        Output:
            {
                'registration': 'ABC1234',
                'vin': '1234567890',
                'make': 'Toyota',
                'model': 'Camry',
                'first_registration_date': '2022-01-01',
                'production_year': 2021,
                'mileage': 10000,
                'fuel_consumption': 9.5,
                'fuel_type_id': 1,
                'vehicle_status_id': 2
            }
        """
        return {
            'registration': self.registration,
            'vin': self.vin,
            'make': self.make,
            'model': self.model,
            'first_registration_date': self.first_registration_date,
            'production_year': self.production_year,
            'mileage': self.mileage,
            'fuel_consumption': self.fuel_consumption,
            'fuel_type_id': self.fuel_type_id,
            'vehicle_status_id': self.vehicle_status_id
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """

        This method is a class method that creates an instance of the class using a dictionary as input.

        Parameters:
            - data (dict[str, Any]): A dictionary containing the necessary data to create an instance of the class.

        Return:
            - Self: An instance of the class with the provided data.

        Example usage:
            data = {
                'registration': 'ABC123',
                'vin': '123456789',
                'make': 'Toyota',
                'model': 'Camry',
                'first_registration_date': '2021-01-01',
                'production_year': 2020,
                'mileage': 10000,
                'fuel_consumption': 8.5,
                'fuel_type_id': 1,
                'vehicle_status_id': 2
            }
            instance = ClassName.from_dict(data)

        """
        return cls(
            data['registration'],
            data['vin'],
            data['make'],
            data['model'],
            data['first_registration_date'],
            data['production_year'],
            data['mileage'],
            data['fuel_consumption'],
            data['fuel_type_id'],
            data['vehicle_status_id']
        )
