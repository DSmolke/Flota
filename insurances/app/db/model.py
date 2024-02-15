from typing import Any, Self
from app.db.configuration import sa


class InsuranceModel(sa.Model):
    """
    InsuranceModel(sa.Model)

    The InsuranceModel class represents an insurance object in the system.

    Attributes:
        __tablename__ (str): The name of the table in the database for storing insurance records.
        id (sa.Column): The primary key column of the insurance table.
        legal_identifier (sa.Column): The legal identifier column of the insurance table.
        start_date (sa.Column): The start date column of the insurance table.
        end_date (sa.Column): The end date column of the insurance table.
        car_registration_number (sa.Column): The car registration number column of the insurance table.
        img_url (sa.Column): The image URL column of the insurance table.
        active (sa.Column): The active status column of the insurance table.

    Methods:
        - as_dict(self) -> dict[str, Any]: Returns the insurance object as a dictionary.
        - save(self) -> None: Saves the current object to the database.
        - delete(self) -> None: Deletes the current instance from the session and commits the changes.
        - update(self, data: dict[str, Any]) -> None: Updates the object attributes with the provided data.
        - get_by_id(cls, insurance_id: int) -> Self: Retrieves the object with the specified ID.
        - get_all(cls) -> list[Self]: Retrieves all objects of the class.

    Usage:
        insurance = InsuranceModel()
        insurance.save()
        insurance.update({'legal_identifier': '12345'})
        insurance.delete()
        insurance_dict = insurance.as_dict()
        insurance_list = InsuranceModel.get_all()
        insurance = InsuranceModel.get_by_id(1)

    """
    __tablename__ = 'insurances'
    id = sa.Column(sa.Integer, primary_key=True)
    legal_identifier = sa.Column(sa.String(25), nullable=False,
                                 unique=True)  # Approx length that I managed to find using web sources was 23
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date, nullable=False)
    car_registration_number = sa.Column(sa.String(7), nullable=False)
    img_url = sa.Column(sa.String(250), nullable=True)
    active = sa.Column(sa.Boolean, nullable=False, default=True)

    def as_dict(self) -> dict[str, Any]:
        """
        Returns the object data as a dictionary.

        :return: A dictionary representing the object data.
        :rtype: dict[str, Any]
        """
        return {
            'id': self.id,
            'legal_identifier': self.legal_identifier,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'car_registration_number': self.car_registration_number,
            'img_url': self.img_url,
            'active': self.active
        }

    def save(self) -> None:
        """
        Save method saves the current object to the database.

        :return: None
        """
        sa.session.add(self)
        sa.session.commit()

    def delete(self) -> None:
        """
        Delete method deletes the current instance from the session and commits the changes.

        :return: None
        """
        sa.session.delete(self)
        sa.session.commit()

    def update(self, data: dict[str, Any]) -> None:
        """
        Updates the object attributes with the provided data.

        :param data: A dictionary containing the data to update the object attributes.
            - 'legal_identifier' (optional): The legal identifier of the object. Defaults to the current legal identifier.
            - 'start_date' (optional): The start date of the object. Defaults to the current start date.
            - 'end_date' (optional): The end date of the object. Defaults to the current end date.
            - 'car_registration_number' (optional): The car registration number of the object. Defaults to the current car registration number.
            - 'active' (optional): The active status of the object. Defaults to the current active status.

        :return: None

        Example usage:
            data = {
                'legal_identifier': '12345',
                'start_date': '2022-01-01',
                'end_date': '2022-12-31',
                'car_registration_number': 'ABC123',
                'active': True
            }
            update(data)
        """
        self.legal_identifier = data.get('legal_identifier', self.legal_identifier)
        self.start_date = data.get('start_date', self.start_date)
        self.end_date = data.get('end_date', self.end_date)
        self.car_registration_number = data.get('car_registration_number', self.car_registration_number)
        self.img_url = data.get('img_url', self.img_url)
        self.active = data.get('active', self.active)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, insurance_id: int) -> Self:
        """
        :param insurance_id: The ID of the desired object to retrieve.
        :return: The object with the specified ID.
        """
        return sa.session.get(cls, {"id": insurance_id})

    @classmethod
    def get_all(cls) -> list[Self]:
        """
        Retrieve all objects of the class.

        :return: A list of objects of the class.
        """
        return [insurance.as_dict() for insurance in sa.session.query(cls).all()]


