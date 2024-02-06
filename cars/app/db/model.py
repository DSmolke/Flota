from typing import Any, Self
from app.db.configuration import sa


class FuelTypeModel(sa.Model):
    """
    Represents a fuel type.

    :param id: The unique identifier of the fuel type.
    :type id: int
    :param name: The name of the fuel type.
    :type name: str
    :param efficiency: The efficiency of the fuel type.
    :type efficiency: float
    """
    __tablename__ = "fuel_type"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(10), unique=True)
    efficiency = sa.Column(sa.Double, nullable=False)

class VehicleStatusModel(sa.Model):
    """

    Class VehicleStatusModel

    This class represents the model for vehicle status in the database.

    Attributes:
    - id: an integer representing the primary key of the vehicle status table.
    - name: a string representing the name of the vehicle status.
    - description: a string representing the description of the vehicle status.

    """
    __tablename__ = "vehicle_status"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20), unique=True)
    description = sa.Column(sa.String(500), nullable=False, unique=True)


class CarModel(sa.Model):
    """
    Represents a car model.

    :param int id: The unique identifier of the car model.
    :param str registration: The registration number of the car model.
    :param str vin: The VIN (Vehicle Identification Number) of the car model.
    :param str make: The make of the car model.
    :param str model: The model of the car model.
    :param date first_registration_date: The date of the first registration of the car model.
    :param str production_year: The production year of the car model.
    :param str mileage: The current mileage of the car model.
    :param str fuel_consumption: The fuel consumption of the car model.
    :param int fuel_type_id: The foreign key referencing the fuel type of the car model.
    :param int vehicle_status_id: The foreign key referencing the vehicle status of the car model.

    :return: An instance of CarModel.
    """
    __tablename__ = 'cars'
    id = sa.Column(sa.Integer, primary_key=True)
    registration = sa.Column(sa.String(10), nullable=False, unique=True)
    vin = sa.Column(sa.String(17), nullable=False, unique=True)
    make = sa.Column(sa.String(100), nullable=False)
    model = sa.Column(sa.String(100), nullable=False)
    first_registration_date = sa.Column(sa.Date, nullable=False)
    production_year = sa.Column(sa.String(4), nullable=False)
    mileage = sa.Column(sa.String(7), nullable=False)
    fuel_consumption = sa.Column(sa.String(5), nullable=False)
    fuel_type_id = sa.Column(sa.Integer, sa.ForeignKey('fuel_type.id'), nullable=False)
    vehicle_status_id = sa.Column(sa.Integer, sa.ForeignKey('vehicle_status.id'), nullable=False)

    def as_dict(self) -> dict[str, Any]:
        """
        Returns the object attributes as a dictionary.

        :return: A dictionary containing the object attributes.
        :rtype: dict
        """
        return {
            'id': self.id,
            'registration': self.registration,
            'vin': self.vin,
            'make': self.make,
            'model': self.model,
            'first_registration_date': self.first_registration_date.isoformat(),
            'production_year': self.production_year,
            'mileage': self.mileage,
            'fuel_type_id': self.fuel_type_id,
            'vehicle_status_id': self.vehicle_status_id,
            'fuel_consumption': self.fuel_consumption
        }

    def save(self) -> None:
        """
        Saves the current object to the database.

        :return: None
        """
        sa.session.add(self)
        sa.session.commit()

    def delete(self) -> None:
        """
        Delete the object from the database.

        :return: None
        """
        sa.session.delete(self)
        sa.session.commit()

    def update(self, data) -> Self:
        """
        Update the attributes of the object with the given data.

        :param data: A dictionary containing the attributes to update.
        :return: The updated object.

        """
        self.registration = data.get('registration', self.registration)
        self.vin = data.get('vin', self.vin)
        self.make = data.get('make', self.make)
        self.model = data.get('model', self.model)
        self.first_registration_date = data.get('first_registration_date', self.first_registration_date)
        self.production_year = data.get('production_year', self.production_year)
        self.mileage = data.get('mileage', self.mileage)
        self.fuel_type_id = data.get('fuel_type_id', self.fuel_type_id)
        self.vehicle_status_id = data.get('vehicle_status_id', self.vehicle_status_id)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, car_id: int) -> 'CarModel':
        """
        :param car_id: The ID of the car that needs to be retrieved.
        :return: A CarModel object representing the car with the specified ID.
        """
        return sa.session.get(cls, {"id": car_id})

    @classmethod
    def get_all(cls) -> list['CarModel']:
        """
        Retrieve all the car models from the database.

        :return: A list of CarModel objects retrieved from the database.
        """
        return [car.as_dict() for car in sa.session.query(cls).all()]
