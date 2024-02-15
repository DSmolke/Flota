def test_create_insurance_with_valid_data(client, insurance_data):
    response = client.post('/insurances', json=insurance_data)
    assert response.status_code == 201
    assert response.json == {**insurance_data, 'id': 1}


def test_create_insurance_with_duplicated_entry(client, insurance_data):
    """
    Test case to verify that creating an insurance with a duplicated entry returns a 403 error
    and the expected error message.

    :param client: The client to make requests to the API
    :param insurance_data: The data for the insurance to be created
    :return: None
    """
    client.post("/insurances", json=insurance_data)
    response2 = client.post("/insurances", json=insurance_data)
    assert response2.status_code == 403
    assert response2.json == {'message': "Duplicate entry 'KPA111111111111' for key 'insurances.legal_identifier'"}


def test_crate_insurance_with_invalid_data(client, insurance_data):
    """
    :param client: The client object to send the HTTP request.
    :param insurance_data: The dictionary containing the insurance data.

    :return: None

    """
    invalid_insurance_data = {**insurance_data, **{'car_registration_number': 'DPL96RR R'}}
    response = client.post("/insurances", json=invalid_insurance_data)
    assert response.status_code == 400
    assert response.json == {'message': "Invalid request"}


def test_get_one_by_id(client, insurance_data):
    """
    Test the 'get_one_by_id' method.

    :param client: The client to make requests.
    :type client: [type]

    :param insurance_data: The data of the insurance to be added.
    :type insurance_data: [type]

    :return: None
    :rtype: None

    :raises AssertionError: When the response JSON does not match the expected result.
    :raises AssertionError: When the response status code is not 200.
    """
    client.post("/insurances", json=insurance_data)
    res = client.get("insurances/1")
    assert res.json == {**insurance_data, 'id': 1}
    assert res.status_code == 200


def test_get_one_by_id_that_not_exist(client):
    """
    :param client: The client object used to send HTTP requests.
    :return: None

    This method tests the behavior of the server when requesting information about a non-existent insurance by its ID. It uses the provided client object to send a GET request to the '/
    *insurances/1' endpoint. The expected behavior is that the server should respond with a 404 status code and a JSON object containing the message "Insurance does not exist". The method
    * includes assertions to verify that the status code and the JSON response match the expected values.
    """
    res = client.get('/insurances/1')
    assert res.status_code == 404
    assert res.json == {"message": "Insurance does not exist"}


def test_delete_insurance_by_id(client, insurance_data):
    """
    Test method for deleting insurance by id.

    :param client: The client object for making requests to the API.
    :param insurance_data: The insurance data to be added to the database.

    :return: None
    """
    client.post("/insurances", json=insurance_data)
    response = client.delete('/insurances/1')
    assert response.status_code == 200
    assert response.json == {"message": "Insurance has been deleted"}


def test_delete_insurance_with_invalid_id(client):
    """
    Delete insurance with invalid id.

    :param client: The test client provided by the test framework.
    :return: None
    """
    response = client.delete('/insurances/1')
    assert response.status_code == 404
    assert response.json == {"message": "Insurance not found"}


def test_get_all(client, insurance_data):
    """
    API test to verify the functionality of retrieving all insurances.

    :param client: The client object for making HTTP requests.
    :param insurance_data: The insurance data to be posted for testing.
    :return: None
    :raises AssertionError: If the response status code is not 200 or the response body does not match the expected JSON.
    """
    client.post("/insurances", json=insurance_data)
    response = client.get("/insurances/all")
    assert response.status_code == 200
    assert response.json == {"all_insurances": [{**insurance_data, 'id': 1}]}


def test_update_insurance_by_id(client, insurance_data):
    """
    Update insurance by ID.

    :param client: The client object used for making HTTP requests.
    :type client: Client

    :param insurance_data: The updated insurance data.
    :type insurance_data: dict

    :return: None
    :rtype: None

    :raises AssertionError: If the response status code is not 200.
    :raises AssertionError: If the response JSON does not match the expected value.

    """
    client.post("/insurances", json=insurance_data)
    response = client.patch("/insurances/1", json={"car_registration_number": "DPL9999"})
    assert response.status_code == 200
    assert response.json == {**insurance_data, 'car_registration_number': 'DPL9999', 'id': 1}


def test_update_insurance_by_id_with_bad_data(client, insurance_data):
    """
    Update insurance data with bad data for a specific insurance ID.

    :param client: A client object used for making HTTP requests.
    :param insurance_data: The updated insurance data to be used for the update request.
    :return: None

    Example usage:
        client = create_client()
        insurance_data = {
            "car_brand": "Toyota",
            "car_registration_number": "ABC1234",
            "insurance_type": "Comprehensive"
        }
        test_update_insurance_by_id_with_bad_data(client, insurance_data)
    """
    client.post('/insurances/1', json=insurance_data)
    response = client.patch("/insurances/1",
                            json={**insurance_data, 'car_registration_number': 'DDD0000 0'})  # regex won't match
    assert response.status_code == 400
    assert response.json == {"message": "Invalid request"}


def test_update_insurance_by_id_when_not_exists(client, insurance_data):
    """
    Test method to update insurance by ID when it does not exist.

    :param client: The test client.
    :type client: object

    :param insurance_data: The insurance data to be updated.
    :type insurance_data: dict

    :return: None
    """
    response = client.patch("/insurances/1", json=insurance_data)
    assert response.status_code == 404
    assert response.json == {"message": "Insurance does not exist"}
