import logging

logging.basicConfig(level=logging.INFO)


class TestCRUDRepairsRoutes:
    def test_create_repair_with_valid_data(self, client, repair_data, desired_response_data) -> None:
        """
        Method to test the create repair endpoint with valid data.

        :param client: The client object to make the HTTP request.
        :param repair_data: The data for creating a repair.
        :param desired_response_data: The expected response data.

        :return: None.
        """
        response = client.post('/repairs', json=repair_data)
        assert response.status_code == 201
        assert response.json == desired_response_data

    def test_get_all_repairs(self, client, repair_data, desired_response_data) -> None:
        """
        Test to verify the functionality of getting all repairs.

        :param client: The test client to make HTTP requests.
        :param repair_data: The data for creating a repair.
        :param desired_response_data: The expected response data for the created repair.
        :return: None
        """
        client.post('/repairs', json=repair_data)
        response = client.get('/repairs/all')
        assert response.status_code == 200
        assert response.json == {'all_repairs': [desired_response_data]}

    def test_get_one_by_id(self, client, repair_data, desired_response_data) -> None:
        """
        Test for retrieving a repair by its ID.

        :param client: The client object to send HTTP requests.
        :type client: object
        :param repair_data: The repair data to be added. It should be in JSON format.
        :type repair_data: dict
        :param desired_response_data: The expected response data that should be returned by the API.
        :type desired_response_data: dict
        :return: None
        """
        client.post('/repairs', json=repair_data)
        response = client.get('/repairs/1')
        assert response.status_code == 200
        assert response.json == desired_response_data

    def test_get_one_by_id_that_not_exist(self, client) -> None:
        """
        Test get_one_by_id_that_not_exist method.

        :param client: The client object.
        :return: None

        """
        res = client.get('/repairs/1')
        assert res.status_code == 404
        assert res.json == {"message": "Repair does not exist"}

    def test_delete_repair_by_id(self, client, repair_data) -> None:
        """
        Deletes a repair by its ID.

        :param client: The client used to make HTTP requests.
        :param repair_data: The data of the repair to be created.
        :return: None
        """
        client.post('/repairs', json=repair_data)
        response = client.delete('/repairs/1')
        assert response.status_code == 200
        assert response.json == {"message": "Repair has been deleted"}

    def test_delete_repair_by_id_when_doesnt_exists(self, client) -> None:
        """
        Test deleting a repair by ID when it doesn't exist.

        :param client: The client to perform the request.
        :return: None
        """
        response = client.delete('/repairs/1')
        assert response.status_code == 404
        assert response.json == {"message": "Repair not found"}

    def test_update_repair_by_id(self, client, repair_data, desired_response_data) -> None:
        """
        Sends a POST request to create a repair with the given repair data,
        then sends a PATCH request to update the repair with the given ID
        by setting the car ID to the specified value. Finally, verifies that
        the response status code is 200 and the response JSON matches the
        expected response data merged with the updated car ID.

        :param client: The test client to send HTTP requests.
        :param repair_data: The data for creating the repair.
        :param desired_response_data: The expected response data after the update.
        :return: None
        """
        client.post('/repairs', json=repair_data)
        response = client.patch('/repairs/1', json={'car_id': 2})
        assert response.status_code == 200
        assert response.json == {**desired_response_data, 'car_id': 2}
#
#
class TestBusinessRepairsRoutes:
    def test_all_repairs_by_car_id(self, client, repair_data) -> None:
        """
        Test the endpoint to get all repairs associated with a car ID.

        :param client: The client to perform HTTP requests.
        :type client: Client
        :param repair_data: The repair data to be used in the test.
        :type repair_data: dict
        :return: None
        """
        repair1 = repair_data
        repair2 = {**repair_data, "repair_description": "Another repair"}
        client.post('/repairs', json=repair1)
        client.post('/repairs', json=repair2)

        response = client.get('/repairs/by_car_id/1')

        assert response.status_code == 200
        assert response.json == {'car_id': 1, 'repairs': [{**repair1, 'id': 1}, {**repair2, 'id': 2}]}

    def test_all_repairs_by_car_id_when_no_entries(self, client) -> None:
        """
        :param client: The HTTP client used to make requests to the server.
        :return: None

        This method tests the behavior of the server when attempting to retrieve all repairs for a specific car with no entries. It uses the provided HTTP client to make a GET request to the
        * "/repairs/by_car_id/1" endpoint. The method then asserts that the response status code is 404 (Not Found) and that the response JSON contains the message "No repairs for that car_id
        *".
        """
        response = client.get('/repairs/by_car_id/1')
        assert response.status_code == 404
        assert response.json == {"message": "No repairs for that car_id"}

    def test_add_pending_repair(self, client, repair_data) -> None:
        """
        Test method to add a pending repair.

        :param client: The client to send the request.
        :param repair_data: The repair data to be added.
        :return: None
        """
        pending_data = {**repair_data, 'repair_status': 2, 'approximate_duration': None}
        response = client.post('/repairs/pending', json=pending_data)
        assert response.status_code == 201
        assert response.json == {**pending_data, 'id': 1}

    def test_start_pending(self, client, repair_data) -> None:
        """
        .. function:: test_start_pending(self, client, repair_data) -> None

            This method is used to test the start_pending function.

            :param client: The HTTP client used to make requests.
            :type client: object

            :param repair_data: The repair data to be used for testing.
            :type repair_data: dict

            :return: None
            :rtype: None

        """
        pending_data = {**repair_data, 'repair_status': 2, 'approximate_duration': None}
        client.post('/repairs/pending', json=repair_data)

        response = client.post('repairs/start_pending/1', json={'approximate_duration': 10})
        assert response.status_code == 201
        assert response.json == {**pending_data, 'id': 1, 'approximate_duration': 10}

    def test_finish_repair(self, client, repair_data, desired_response_data) -> None:
        """
        Test the finish repair endpoint.

        :param client: The test client.
        :param repair_data: The data for creating a repair.
        :param desired_response_data: The expected response data.
        :return: None.
        """
        client.post('/repairs', json=repair_data)
        response = client.post('/repairs/finish/1')
        assert response.status_code == 201
        assert response.json == {**desired_response_data, 'repair_status': 3}

    def test_finish_repair_when_repair_does_not_exist(self, client, repair_data, desired_response_data) -> None:
        """
        Test if finishing a repair that does not exist returns a 404 status code and the correct error message.

        :param client: The test client.
        :param repair_data: The data for the repair.
        :param desired_response_data: The desired response data.
        :return: None.
        """
        response = client.post('/repairs/finish/1')
        assert response.status_code == 404
        assert response.json == {"message": "Repair not found"}