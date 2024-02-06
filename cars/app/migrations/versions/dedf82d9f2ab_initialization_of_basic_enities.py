"""Initialization of basic enities

Revision ID: dedf82d9f2ab
Revises: f6e6c9eebc4b
Create Date: 2024-01-25 00:02:37.290040

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dedf82d9f2ab'
down_revision = 'f6e6c9eebc4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO db_1.fuel_type(name, efficiency) values 
        ('petrol', 0.89),
        ('diesel', 0.95),
        ('electric', 0.7)
        """
    )

    op.execute(
        """
        INSERT INTO db_1.vehicle_status(name, description) values 
        ('ready', 'Ready to use'),
        ('repair', 'Waiting for repairs to be done'),
        ('not_legal', 'Waiting for mot or insurance')
        """
    )

    op.execute(
        """
        INSERT INTO db_1.cars(
            registration,
            vin,
            make,
            model,
            first_registration_date,
            production_year,
            mileage,
            fuel_consumption,
            fuel_type_id,
            vehicle_status_id
            ) values (
                'WA38900',
                'VF3MJEHZRJS446751',
                'Peugeot',
                '308',
                '2017-08-21',
                2017,
                150000,
                5.6,
                1,
                1
            ),
            (
                'WZ38900',
                'GF3MJE5ZRJS416751',
                'Ford',
                'Focus',
                '2021-08-21',
                2020,
                15000,
                7.9,
                1,
                1
            )
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM db_1.cars
        """
    )

    op.execute(
        """
        DELETE FROM db_1.fuel_type
        """
    )

    op.execute(
        """
        DELETE FROM db_1.vehicle_status
        """
    )
