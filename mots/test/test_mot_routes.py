import logging

logging.basicConfig(level=logging.INFO)


def test_create_mot_with_valid_data(client, mot_data):
    """
    Test the creation of a MOT with valid data.

    :param client: HTTP client for making requests.
    :param mot_data: Dictionary containing MOT data.
    :return: None.
    """
    response = client.post('/mots', json=mot_data)
    assert response.status_code == 201
    assert response.json == {**mot_data, 'id': 1}

def test_create_mot_with_duplicated_entry(client, mot_data):
    """
    Test case to verify the behavior of creating a MOT with a duplicated entry.

    :param client: The test client.
    :type client: Client
    :return: None
    :rtype: None
    """

    client.post("/mots", json=mot_data)
    response2 = client.post("/mots", json=mot_data)
    assert response2.status_code == 403
    assert response2.json == {'message': "Duplicate entry 'XXX/XXX/XXX/XXXX/XXXX' for key 'mots.legal_identifier'"}

def test_crate_mot_with_invalid_data(client, mot_data):
    """
    :param client: The client object used to make POST requests to create MOTs.
    :param mot_data: The data containing the information for the MOT to be created.

    :return: None

    This method is used to test the creation of MOTs with invalid data. It takes in a client object and mot_data as parameters.
    It creates invalid_mot_data by merging the mot_data with an additional key-value pair where car_registration_number is set
    to 'DPL96RR R'. It then makes a POST request to "/mots" endpoint with the invalid_mot_data as the payload.

    The method asserts that the response status code is 400, indicating a bad request, and the response body is {'message': "Invalid request"}.
    """
    invalid_mot_data = {**mot_data, ** {'car_registration_number': 'DPL96RR R'}}
    response = client.post("/mots", json=invalid_mot_data)
    assert response.status_code == 400
    assert response.json == {'message': "Invalid request"}


def test_get_one_by_id(client, mot_data):
    """
    Test the 'get_one_by_id' method.

    :param client: The client used to send HTTP requests.
    :param mot_data: The data used to create a MOT.
    :return: None.
    """
    client.post("/mots", json=mot_data)
    res = client.get("mots/1")
    assert res.json == {**mot_data, 'id': 1}
    assert res.status_code == 200


def test_get_one_by_id_that_not_exist(client):
    """
    Test the get_one_by_id method when the MOT does not exist.

    :param client: The test client.
    :return: None.
    """
    res = client.get('/mots/1')
    assert res.status_code == 404
    assert res.json == {"message": "Mot does not exist"}

def test_delete_mot_by_id(client, mot_data):
    """
    Delete a Mot by ID from the server.

    :param client: The test client for making requests to the server.
    :param mot_data: The data of the Mot to be created before deletion.
    :return: None
    """
    client.post("/mots", json=mot_data)
    response = client.delete('/mots/1')
    assert response.status_code == 200
    assert response.json == {"message": "Mot has been deleted"}


def test_delete_mot_with_invalid_id(client):
    """
    Delete Method - test_delete_mot_with_invalid_id

    Deletes a Mot with an invalid ID from the server.

    :param client: The client object to make requests to the server.
    :return: None

    """
    response = client.delete('/mots/1')
    assert response.status_code == 404
    assert response.json == {"message": "Mot not found"}

def test_get_all(client, mot_data):
    """
    Test the "get_all" method of a client.

    :param client: The client to test.
    :type client: object
    :param mot_data: The data to post as a MOT.
    :type mot_data: dict
    :return: None
    :rtype: None
    """
    client.post("/mots", json=mot_data)
    response = client.get("/mots/all")
    assert response.status_code == 200
    assert response.json == {"all_mots": [{**mot_data, 'id': 1}]}


def test_update_mot_by_id(client, mot_data):
    """
    Test method to update a MOT by its ID.

    :param client: The client for making HTTP requests.
    :type client: obj
    :param mot_data: The data of the MOT to be updated.
    :type mot_data: dict
    :return: None
    :rtype: None
    """
    client.post("/mots", json=mot_data)
    response = client.patch("/mots/1", json={"car_registration_number": "DPL9999"})
    assert response.status_code == 200
    assert response.json == {**mot_data, 'car_registration_number': 'DPL9999', 'id': 1}

def test_update_mot_by_id_with_bad_data(client, mot_data):
    """
    Test the update_mot_by_id_with_bad_data method.

    :param client: The client object used to send HTTP requests.
    :param mot_data: The updated MOT data to be sent in the request.
    :return: None

    This method tests the behavior of the update_mot_by_id_with_bad_data method by sending a POST request to create a MOT with the provided data, followed by a PATCH request to update the
    * MOT with invalid data.
    The PATCH request should return a 400 HTTP status code and a JSON response with the"""
    client.post('/mots/1', json=mot_data)
    response = client.patch("/mots/1", json={**mot_data, 'car_registration_number': 'DDD0000 0'}) # regex won't match
    assert response.status_code == 400
    assert response.json == {"message": "Invalid request"}

def test_update_mot_by_id_when_not_exists(client, mot_data):
    """
    Test case to verify the behavior of the method when attempting to update a Mot that does not exist.

    :param client: The client used to make the request.
    :type client: Whatever type is the client parameter.
    :param mot_data: The data to be included in the request payload.
    :type mot_data: Whatever type is the mot_data parameter.
    :return: None
    :rtype: None

    :raises AssertionError: If the response status code is not 404 or if the response json is not equal to
                            {"message": "Mot does not exist"}.
    """
    response = client.patch("/mots/1", json=mot_data)
    assert response.status_code == 404
    assert response.json == {"message": "Mot does not exist"}

