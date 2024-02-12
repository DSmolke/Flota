from typing import Any, Self
from app.db.configuration import sa


class MotModel(sa.Model):
    """
    This class represents a model for MOTs (Ministry of Transport tests) in a database.

    :class:`MotModel`
        This class inherits from `sa.Model`.

    Attributes:
        __tablename__ (str): The name of the table in the database where MOT records are stored.
        id (sa.Column): Primary key column representing the MOT ID.
        legal_identifier (sa.Column): Column representing the legal identifier of the MOT.
        start_date (sa.Column): Column representing the start date of the MOT.
        end_date (sa.Column): Column representing the end date of the MOT.
        car_registration_number (sa.Column): Column representing the car registration number associated with the MOT.
        active (sa.Column): Column representing the active status of the MOT.


    ```
    """
    __tablename__ = 'mots'
    id = sa.Column(sa.Integer, primary_key=True)
    legal_identifier = sa.Column(sa.String(25), nullable=False,
                                 unique=True)  # Approx length that I managed to find using web sources was 23
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date, nullable=False)
    car_registration_number = sa.Column(sa.String(7), nullable=False)
    img_url = sa.Column(sa.String(250), nullable=True)
    active = sa.Column(sa.Boolean, nullable=False, default=True)

    def as_dict(self) -> dict[str, Any]:
        """Return the object as a dictionary.

        :return: A dictionary representation of the object.
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
    def get_by_id(cls, mot_id: int) -> Self:
        """
        :param mot_id: The ID of the desired object to retrieve.
        :return: The object with the specified ID.
        """
        return sa.session.get(cls, {"id": mot_id})

    @classmethod
    def get_all(cls) -> list[Self]:
        """
        Retrieve all objects of the class.

        :return: A list of objects of the class.
        """
        return [mot.as_dict() for mot in sa.session.query(cls).all()]
