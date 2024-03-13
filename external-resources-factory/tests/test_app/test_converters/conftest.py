import pytest


@pytest.fixture(scope="session")
def two_elements_valid_car_data():
    """
    This method returns a list of two dictionaries, where each dictionary represents valid car data.

    The car data is structured as follows:

    - registration: a string representing the registration number of the car
    - vin: a string representing the vehicle identification number (VIN) of the car
    - make: a string representing the make of the car
    - model: a string representing the model of the car
    - first_registration_date: a string representing the date of the first registration of the car (format: YYYY-MM-DD)
    - production_year: a string representing the production year of the car
    - mileage: a string representing the mileage of the car
    - fuel_consumption: a string representing the fuel consumption of the car
    - fuel_type_id: a string representing the ID of the fuel type of the car
    - vehicle_status_id: a string representing the ID of the vehicle status of the car

    Example usage:

    data = two_elements_valid_car_data()

    Output:
    [
        {
            "registration": "DPL96RR",
            "vin": "4Y1SL65848Z411439",
            "make": "BMW",
            "model": "SERIES 3",
            "first_registration_date": "2012-03-15",
            "production_year": "2012",
            "mileage": "2000",
            "fuel_consumption": "5.5",
            "fuel_type_id": "1",
            "vehicle_status_id": "1"
        },
        {
            "registration": "DPL96RL",
            "vin": "4Y1SL65848Z411419",
            "make": "BMW",
            "model": "SERIES 4",
            "first_registration_date": "2019-03-15",
            "production_year": "2019",
            "mileage": "2000",
            "fuel_consumption": "7",
            "fuel_type_id": "1",
            "vehicle_status_id": "1"
        }
    ]
    """
    data = [
        {
            "registration": "DPL96RR",
            "vin": "4Y1SL65848Z411439",
            "make": "BMW",
            "model": "SERIES 3",
            "first_registration_date": "2012-03-15",
            "production_year": "2012",
            "mileage": "2000",
            "fuel_consumption": "5.5",
            "fuel_type_id": "1",
            "vehicle_status_id": "1"

        },
        {
            "registration": "DPL96RL",
            "vin": "4Y1SL65848Z411419",
            "make": "BMW",
            "model": "SERIES 4",
            "first_registration_date": "2019-03-15",
            "production_year": "2019",
            "mileage": "2000",
            "fuel_consumption": "7",
            "fuel_type_id": "1",
            "vehicle_status_id": "1"
        }
    ]
    return data
