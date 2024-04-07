import logging

logging.basicConfig(level=logging.INFO)


class TestCRUDDriversRoutes:
    def test_create_driver_with_valid_data(self, client, driver_data, desired_response_data) -> None:

        response = client.post('/driver', json=driver_data)
        assert response.status_code == 201
        assert response.json == desired_response_data

    def test_get_all_drivers(self, client, driver_data, desired_response_data) -> None:

        client.post('/driver', json=driver_data)
        response = client.get('/drivers/all')
        assert response.status_code == 200
        assert response.json == {'all_drivers': [desired_response_data]}

    def test_get_one_by_id(self, client, driver_data, desired_response_data) -> None:

        client.post('/driver', json=driver_data)
        response = client.get('/driver/1')
        assert response.status_code == 200
        assert response.json == desired_response_data

    def test_get_one_by_id_that_not_exist(self, client) -> None:

        res = client.get('/driver/1')
        assert res.status_code == 404
        assert res.json == {"message": "Driver does not exist"}

    def test_delete_driver_by_id(self, client, driver_data) -> None:

        client.post('/driver', json=driver_data)
        response = client.delete('/driver/1')
        assert response.status_code == 200
        assert response.json == {"message": "Driver has been deleted"}

    def test_delete_driver_by_id_when_doesnt_exists(self, client) -> None:

        response = client.delete('/driver/1')
        assert response.status_code == 404
        assert response.json == {"message": "Driver not found"}

    def test_update_driver_by_id(self, client, driver_data, desired_response_data) -> None:

        client.post('/driver', json=driver_data)
        response = client.patch('/driver/1', json={'email': 'd.smolczynski@o2.pl'})
        assert response.status_code == 200
        assert response.json == {**desired_response_data, 'email': 'd.smolczynski@o2.pl'}
