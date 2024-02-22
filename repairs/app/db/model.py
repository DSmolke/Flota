from typing import Self, Any
from app.db.configuration import sa


class RepairStatus(sa.Model):
    __tablename__ = 'repair_status'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(7), nullable=False)


class RepairModel(sa.Model):
    """
    Module: repair_model

    Description:
    This module contains the `RepairModel` class, which represents a repair record in a database. The class provides methods for CRUD operations on repair records.

    Classes:
    - `RepairModel`: A class representing a repair record.

    Methods:
    - `as_dict()`: Converts the `RepairModel` object to a dictionary representation.
    - `save()`: Saves the `RepairModel` object to the database.
    - `delete()`: Deletes the `RepairModel` object from the database.
    - `update(data: dict[str, Any])`: Updates the `RepairModel` object with the provided data.
    - `get_by_id(repair_id: int) -> RepairModel`: Retrieves a repair record by its ID.
    - `get_all_by_car_id(car_id: int) -> list[RepairModel]`: Retrieves all repair records associated with a specific car ID.
    - `get_all() -> list[RepairModel]`: Retrieves all repair records.

    Usage:

    ```python
    from repair_model import RepairModel

    # Example usage
    repair = RepairModel()
    repair.car_id = 1
    repair.repair_status = 2
    repair.repair_description = 'Engine oil change'
    repair.start_date = '2022-01-01'
    repair.approximate_duration = 1
    repair.garage_name = 'Example Garage'
    repair.garage_phone = '123-456-7890'

    repair.save()

    repair.repair_description = 'Oil and filter change'
    repair.update({'repair_status': 3})

    repair.delete()

    found_repair = RepairModel.get_by_id(1)
    all_repairs = RepairModel.get_all()
    ```
    """
    __tablename__ = 'repairs'
    id = sa.Column(sa.Integer, primary_key=True)
    car_id = sa.Column(sa.Integer, nullable=False)
    repair_status = sa.Column(sa.Integer, sa.ForeignKey('repair_status.id'), nullable=False)
    repair_description = sa.Column(sa.String(500), nullable=False)
    start_date = sa.Column(sa.Date)
    approximate_duration = sa.Column(sa.Integer)
    garage_name = sa.Column(sa.String(100), nullable=False)
    garage_phone = sa.Column(sa.String(13), nullable=False)

    def as_dict(self) -> dict[str, Any]:
        """
        Return the object attributes as a dictionary.

        :return: A dictionary containing the object attributes.
        :rtype: dict[str, Any]
        """
        return {
            'id': self.id,
            'car_id': self.car_id,
            'repair_status': self.repair_status,
            'repair_description': self.repair_description,
            'start_date': self.start_date.isoformat(),
            'approximate_duration': self.approximate_duration,
            'garage_name': self.garage_name,
            'garage_phone': self.garage_phone
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
        Updates the attributes of the current object with the given data.

        :param data: A dictionary containing the updated values for the following attributes:
            - car_id (Optional): The ID of the car associated with the repair.
            - repair_status (Optional): The status of the repair.
            - repair_description (Optional): A description of the repair.
            - start_date (Optional): The start date of the repair.
            - approximate_duration (Optional): The approximate duration of the repair.
            - garage_name (Optional): The name of the garage where the repair is being done.
            - garage_phone (Optional): The phone number of the garage.

        :return: None

        Example usage:

            data = {
                'car_id': 123,
                'repair_status': 1,
                'repair_description': 'Engine repair',
                'start_date': '2022-01-01',
                'approximate_duration': 5,
                'garage_name': 'ABC Garage',
                'garage_phone': '570688764'
            }
            update(data)
        """
        self.car_id = data.get('car_id', self.car_id)
        self.repair_status = data.get('repair_status', self.repair_status)
        self.repair_description = data.get('repair_description', self.repair_description)
        self.start_date = data.get('start_date', self.start_date)
        self.approximate_duration = data.get('approximate_duration', self.approximate_duration)
        self.garage_name = data.get('garage_name', self.garage_name)
        self.garage_phone = data.get('garage_phone', self.garage_phone)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, repair_id: int) -> Self:
        """
        Returns a repair object with the specified repair_id.

        :param repair_id: The ID of the repair object to retrieve.
        :type repair_id: int
        :return: The repair object with the specified repair_id.
        :rtype: Self
        """
        return sa.session.get(cls, {"id": repair_id})

    @classmethod
    def get_all_by_car_id(cls, car_id: int) -> list[Self]:
        """
        Retrieve all repairs by car ID.

        :param car_id: The ID of the car for which repairs are retrieved.
        :return: A list of repair objects associated with the specified car ID.
        """
        found_repairs = sa.session.execute(sa.select(cls).filter_by(car_id=car_id)).scalars()
        if found_repairs:
            return [repair.as_dict() for repair in found_repairs]
        return []

    @classmethod
    def get_all(cls) -> list[Self]:
        """
        Retrieves all instances of the class.

        :return: A list of instances of the class.
        :rtype: list
        """
        return [repair.as_dict() for repair in sa.session.query(cls).all()]
