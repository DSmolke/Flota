from typing import Self, Any
from app.db.configuration import sa


class DriverModel(sa.Model):
    """

    The `DriverModel` class represents a model for drivers in a database.

    Attributes:
        - `id`: Integer, primary key of the driver.
        - `first_name`: String, first name of the driver.
        - `last_name`: String, last name of the driver.
        - `phone_number`: String, phone number of the driver.
        - `email`: String, email of the driver.
        - `car_registration`: String, car registration of the driver.

    Constraints:
        - `driver_constraint`: Unique constraint that ensures the combination of first name, last name, and car registration is unique.

    Methods:
        - `as_dict() -> dict[str, Any]`: Returns the driver's attributes as a dictionary.
        - `save() -> None`: Saves the current driver object to the database.
        - `delete() -> None`: Deletes the current driver instance from the database.
        - `update(data: dict[str, Any]) -> None`: Updates the driver's attributes with the provided data dictionary and saves the changes to the database.
        - `get_by_id(driver_id: int) -> Self`: Returns the driver instance with the specified ID.
        - `get_all() -> list[Self]`: Returns a list of all drivers in the database.

    """
    __tablename__ = 'drivers'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(50), nullable=False)
    last_name = sa.Column(sa.String(50), nullable=False)
    phone_number = sa.Column(sa.String(9), nullable=False)
    email = sa.Column(sa.String(500), nullable=False)
    car_registration = sa.Column(sa.String(7), nullable=False)

    driver_constraint = sa.UniqueConstraint(first_name, last_name, car_registration)

    def as_dict(self) -> dict[str, Any]:
        """
        Return the object as a dictionary.

        :return: A dictionary representation of the object, containing the following attributes:
            - 'id': The unique identifier of the object.
            - 'first_name': The first name of the object.
            - 'last_name': The last name of the object.
            - 'phone_number': The phone number of the object.
            - 'email': The email address of the object.
            - 'car_registration': The car registration information of the object.
        :rtype: dict[str, Any]
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'car_registration': self.car_registration
        }

    def save(self) -> None:
        """Save the current object to the database.

        :return: None
        """
        sa.session.add(self)
        sa.session.commit()

    def delete(self) -> None:
        """
        Delete the current instance from the database.

        :return: None

        """
        sa.session.delete(self)
        sa.session.commit()

    def update(self, data: dict[str, Any]) -> None:
        """
        Updates the attributes of the object with the given data.

        :param data: A dictionary containing the updated attribute values. The keys of the dictionary corresponds to the attribute names, and the values corresponds to the new values.
        :return: None
        """
        self.first_name = data.get('first_name', self.first_name)
        self.last_name = data.get('last_name', self.last_name)
        self.phone_number = data.get('phone_number', self.phone_number)
        self.email = data.get('email', self.email)
        self.car_registration = data.get('car_registration', self.car_registration)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, driver_id: int) -> Self:
        """
        Retrieve a driver object by its id.

        :param driver_id: The id of the driver
        :type driver_id: int
        :return: The driver object with the given id
        :rtype: Self
        """
        return sa.session.get(cls, {"id": driver_id})

    @classmethod
    def get_all(cls) -> list[Self]:
        """
        Retrieve all instances of the class.

        :return: A list containing all instances of the class.
        :rtype: list
        """
        return [driver.as_dict() for driver in sa.session.query(cls).all()]
