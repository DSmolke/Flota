import logging

logging.basicConfig(level=logging.INFO)


class TestCRUDDriversRoutes:
    """
    Test the creation of a driver with valid data.

    :param client: The client object to make HTTP requests.
    :param driver_data: The data of the driver to be created.
    :param desired_response_data: The expected response data upon successful creation of the driver.
    :return: None
    """
    def test_create_driver_with_valid_data(self, client, driver_data, desired_response_data) -> None:
        """
        :param client: The client object used for making the HTTP request.
        :type client: object

        :param driver_data: The data representing the driver to be created.
        :type driver_data: dict

        :param desired_response_data: The expected response data after creating the driver.
        :type desired_response_data: dict

        :return: None
        :rtype: None

        This method tests the creation of a driver with valid data by making an HTTP POST request to the '/driver' endpoint using the provided client object and driver data. It then asserts
        * that the response status code is equal to 201 (indicating successful creation) and that the response data matches the desired_response_data.

        Example usage:
            client = create_client()
            driver_data = {'name': 'John Doe', 'license_number': 'ABC123'}
            desired_response_data = {'id': 1, 'name': 'John Doe', 'license_number': 'ABC123'}
            test_create_driver_with_valid_data(client, driver_data, desired_response_data)

        Raises:
            AssertionError: If the response status code is not equal to 201 or the response data does not match the desired_response_data.
        """
        response = client.post('/driver', json=driver_data)
        assert response.status_code == 201
        assert response.json == desired_response_data

    def test_get_all_drivers(self, client, driver_data, desired_response_data) -> None:
        """
        Test the get all drivers API endpoint.

        :param client: The client object for making HTTP requests.
        :param driver_data: The JSON data of the driver to be created.
        :param desired_response_data: The expected JSON response data containing the driver information.
        :return: None
        """
        client.post('/driver', json=driver_data)
        response = client.get('/drivers/all')
        assert response.status_code == 200
        assert response.json == {'all_drivers': [desired_response_data]}

    def test_get_one_by_id(self, client, driver_data, desired_response_data) -> None:
        """
        :param client: The client object used for sending HTTP requests.
        :param driver_data: The data for creating a driver object.
        :param desired_response_data: The expected data in the response.

        :return: None

        """
        client.post('/driver', json=driver_data)
        response = client.get('/driver/1')
        assert response.status_code == 200
        assert response.json == desired_response_data

    def test_get_one_by_id_that_not_exist(self, client) -> None:
        """
        Test the behavior of the `get_one_by_id` method when the driver does not exist.

        :param client: The client used to make requests.
        :return: None
        """
        res = client.get('/driver/1')
        assert res.status_code == 404
        assert res.json == {"message": "Driver does not exist"}

    def test_delete_driver_by_id(self, client, driver_data) -> None:
        """
        .. py:method:: test_delete_driver_by_id(client, driver_data) -> None

           This method tests the deletion of a driver by ID.

           :param client: A client object used for making HTTP requests.
           :type client: object
           :param driver_data: The data of the driver to be deleted.
           :type driver_data: dict
           :return: None
           :rtype: None

           :Example:

           .. code-block:: python

              client = create_test_client()
              driver_data = {
                  "id": 1,
                  "name": "John Doe",
                  "license": "ABC123"
              }
              test_delete_driver_by_id(client, driver_data)
        """
        client.post('/driver', json=driver_data)
        response = client.delete('/driver/1')
        assert response.status_code == 200
        assert response.json == {"message": "Driver has been deleted"}

    def test_delete_driver_by_id_when_doesnt_exists(self, client) -> None:
        """
        :param client: The client object used to make the HTTP request.
        :return: None

        Deletes a driver with the given ID when it doesn't exist.

        This method sends a DELETE request to the '/driver/1' endpoint of the client object to delete a driver with ID '1'. It then asserts that the response status code is 404 (Not Found) and
        * the response JSON contains a message indicating that the driver was not found.
        """
        response = client.delete('/driver/1')
        assert response.status_code == 404
        assert response.json == {"message": "Driver not found"}

    def test_update_driver_by_id(self, client, driver_data, desired_response_data) -> None:
        """
        :param client: the client object used to send requests to the API
        :param driver_data: the data of the driver to be updated
        :param desired_response_data: the expected data of the response

        :return: None

        Test method to verify the functionality of updating a driver by ID.

        1. Sends a POST request to create a new driver using client object and driver_data.
        2. Sends a PATCH request to update the driver with ID=1 using client object and the provided email in the request payload.
        3. Asserts that the response status code is 200, indicating a successful update.
        4. Asserts that the response JSON data matches the desired_response_data merged with the provided email in the request payload.
        """
        client.post('/driver', json=driver_data)
        response = client.patch('/driver/1', json={'email': 'd.smolczynski@o2.pl'})
        assert response.status_code == 200
        assert response.json == {**desired_response_data, 'email': 'd.smolczynski@o2.pl'}
