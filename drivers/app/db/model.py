from typing import Self, Any
from app.db.configuration import sa


class DriverModel(sa.Model):
    __tablename__ = 'drivers'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(50), nullable=False)
    last_name = sa.Column(sa.String(50), nullable=False)
    phone_number = sa.Column(sa.String(9), nullable=False)
    email = sa.Column(sa.String(500), nullable=False)
    car_registration = sa.Column(sa.String(7), nullable=False)

    driver_constraint = sa.UniqueConstraint(first_name, last_name, car_registration)

    def as_dict(self) -> dict[str, Any]:
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
        self.first_name = data.get('first_name', self.first_name)
        self.last_name = data.get('last_name', self.last_name)
        self.phone_number = data.get('phone_number', self.phone_number)
        self.email = data.get('email', self.email)
        self.car_registration = data.get('car_registration', self.car_registration)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, driver_id: int) -> Self:
        return sa.session.get(cls, {"id": driver_id})

    @classmethod
    def get_all(cls) -> list[Self]:
        return [driver.as_dict() for driver in sa.session.query(cls).all()]
