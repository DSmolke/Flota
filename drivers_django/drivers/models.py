from django.db import models

class DriverModel(models.Model):
    """
    The DriverModel class is a model class that represents a driver in the application.

    Attributes:
        first_name (CharField): The first name of the driver.
        last_name (CharField): The last name of the driver.
        phone_number (CharField): The phone number of the driver.
        email (CharField): The email address of the driver.
        car_registration (CharField): The car registration number of the driver.

    Meta:
        managed (bool): Specifies whether the table for this model is managed by the database.
        db_table (str): The name of the database table for this model.
        unique_together (list): Specifies the fields that must be unique together.

    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    email = models.CharField(max_length=500)
    car_registration = models.CharField(max_length=7)

    class Meta:
        """

        Class Meta

        This class represents the meta options for the "drivers" database table.

        Attributes:
            managed (bool): Specifies whether this table is managed by Django.
                            Defaults to False.
            db_table (str): The name of the database table to use for this model.
                            Defaults to 'drivers'.
            unique_together (tuple): Specifies the fields that together must be unique.
                                     Defaults to (('first_name', 'last_name', 'car_registration'),).

        """
        managed = False
        db_table = 'drivers'
        unique_together = (('first_name', 'last_name', 'car_registration'),)
