from app.service.models import CarDetails


def test_as_dict():
    """

    :return: (dict) Returns a dictionary representation of the CarDetails object.

    """
    car = CarDetails("DPL29742", "WVWZZZ3CZ6E101738", "23.03.2006")
    assert car.as_dict() == {
        "registration": "DPL29742",
        "vin": "WVWZZZ3CZ6E101738",
        "first_registration_date": "23.03.2006"
    }
