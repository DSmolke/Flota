import logging

logging.basicConfig(level=logging.INFO)

def test_create_car_with_valid_data(client, car_data):
    """
    Test method to create a car with valid data.

    :param client: The test client for making requests.
    :param car_data: The data for creating the car in JSON format.
    :return: None
    """
    response = client.post("/car", json=car_data)
    assert response.status_code == 201
    assert response.json == 1


def test_create_car_with_duplicated_entry(client, car_data):
    """
    Method to test the creation of a car with duplicated entry.

    :param client: The client object for making HTTP requests.
    :type client: flask.testing.FlaskClient
    :param car_data: The data for creating the car.
    :type car_data: dict
    :return: None
    """
    client.post("/car", json=car_data)
    response2 = client.post("/car", json=car_data)
    assert response2.status_code == 403
    assert response2.json == {'message': "Duplicate entry 'DPL96RR' for key 'cars.registration'"}


def test_crate_car_with_invalid_data(client, car_data):
    """
    :param client: The client object used to send the HTTP request
    :param car_data: The data used to create the car
    :return: None

    This method is used to test the creation of a car with invalid data. It takes a `client` object and `car_data` as
    parameters. The `client` object is used to send an HTTP POST request
    * to the `/car` endpoint with the `car_data`. The `car_data` is modified by updating the `"registration"`
     field to an invalid value.

    The method then asserts that the response status code is 400 (Bad Request) and
    the response JSON is `{'message': "Invalid request"}`.
    """
    invalid_car_data = {**car_data}
    invalid_car_data.update({"registration": "DPL96RR R"})
    response = client.post("/car", json=invalid_car_data)
    assert response.status_code == 400
    assert response.json == {'message': "Invalid request"}


def test_get_one_by_id(client, car_data, desired_response_data):
    """
    Test the GET /car/<id> endpoint for retrieving a car by ID.

    :param client: The test client.
    :param car_data: The car data to be posted.
    :param desired_response_data: The expected response data.
    :return: None.
    """
    client.post("/car", json=car_data)
    res = client.get("car/1")
    assert res.json == desired_response_data
    assert res.status_code == 200

def test_get_one_by_id_that_not_exist(client):
    """
    Test method to check if getting a car by id that does not exist returns a 404 status code and a proper error message.

    :param client: The HTTP client to use for sending requests.
    :return: None
    """
    res = client.get('/car/1')
    assert res.status_code == 404
    assert res.json == {"message": "Car does not exist"}

def test_delete_car_by_id(client, car_data):
    """
    Test deleting a car by its ID.

    :param client: The Flask test client.
    :type client: flask.testing.FlaskClient
    :param car_data: The data of the car to be created.
    :type car_data: dict
    :return: None
    """
    client.post("/car", json=car_data)
    response = client.delete('/car/1')
    assert response.status_code == 200
    assert response.json == {"message": "Car has been deleted"}


def test_delete_car_with_invalid_id(client):
    """
    Test deleting a car that doesn't exist

    :param client: A Flask test client object.
    :return: None

    """
    response = client.delete('/car/1')
    assert response.status_code == 404
    assert response.json == {"message": "Car not found"}


def test_get_all_cars(client, car_data, desired_response_data):
    """
    Test the 'GET /cars/all' endpoint to retrieve all cars.

    :param client: The test client for making HTTP requests.
    :param car_data: The JSON data of the car to be posted.
    :param desired_response_data: The expected JSON data of the desired car response.
    :return: None
    """
    client.post("/car", json=car_data)
    response = client.get("/cars/all")
    assert response.status_code == 200
    assert response.json == {"all_cars": [desired_response_data]}


def test_update_car_by_id(client, car_data, desired_response_data):
    """
    Test the update_car_by_id method.

    :param client: The client object used for making HTTP requests.
    :type client: object
    :param car_data: The data of the car to be updated.
    :type car_data: dict
    :param desired_response_data: The desired response data that after creation of entity contains id.
    :type desired_response_data: dict
    :return: None

    """

    client.post("/car", json=car_data)
    response = client.patch("/car/1", json={"registration": "XXXXXXX"})
    assert response.status_code == 200
    assert response.json == {**desired_response_data, 'registration': 'XXXXXXX'}

def test_update_car_by_id_with_bad_data(client, car_data):
    """
    Test the update_car_by_id_with_bad_data method.

    :param client: The client used to send the request.
    :param"""
    client.post('/car/1', json=car_data)
    response = client.patch("/car/1", json={**car_data, 'registration': 'DDD0000 0'}) # regex won't match
    assert response.status_code == 400
    assert response.json == {"message": "Invalid request"}


def test_update_car_by_id_when_not_exists(client, car_data):
    """

    :param client: The client used to send the HTTP request.
    :type client: object

    :param car_data: The data of the car to be updated.
    :type car_data: dict

    :return: None

    """
    response = client.patch("/car/1", json=car_data)
    assert response.status_code == 404
    assert response.json == {"message": "Car does not exist"}
