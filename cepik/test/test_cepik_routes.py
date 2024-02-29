from app.service.cepik_service import CepikSevice

class TestCarStatusRoute:
    """
    The `TestCarStatusRoute` class contains test cases for the `car_status` route.

    Methods:
    - `test_car_status_successful_response(client, mocker) -> None`: This method tests the successful response of the `car_status` route. It mocks the necessary dependencies and asserts
    * that the response status code is 200 and the JSON response matches the expected result.

    - `test_car_status_with_unsuccessful_response(client, mocker) -> None`: This method tests the unsuccessful response of the `car_status` route. It mocks the necessary dependencies and
    * asserts that the response status code is 400 and the JSON response contains an error message.

    """
    def test_car_status_successful_response(self, client, mocker) -> None:
        """
        Test successful response for car status.

        :param client: The client for making HTTP requests.
        :param mocker: The mocker object for patching methods.
        :return: None
        """
        mocker.patch('app.routes.cepik.map_report_result', side_effect=lambda *args, **kwargs: {
            "insurance_valid": True,
            "mot_valid": True
        }, create=True)

        mocker.patch.object(CepikSevice, '__init__', lambda *args, **kwargs: None)
        mocker.patch.object(CepikSevice, 'get_car_report', lambda *args, **kwargs: None)

        response = client.get('/car_status', json={
            "registration": "DPL29742",
            "vin": "WVWZZZ3CZ6E101738",
            "first_registration_date": "23.03.2006"
        })
        assert response.status_code == 200
        assert response.get_json() == {
            "insurance_valid": True,
            "mot_valid": True
        }

    def test_car_status_with_unsuccessful_response(self, client, mocker) -> None:
        """
        Test the car status endpoint with an unsuccessful response.

        :param client: The test client for making HTTP requests.
        :param mocker: The mocker object for patching the CepikSevice class.
        :return: None

        Example usage:

        .. code-block:: python

            def test_car_status_with_unsuccessful_response(self, client, mocker) -> None:
                mocker.patch.object(CepikSevice, '__init__', lambda *args, **kwargs: Exception())
                response = client.get('/car_status', json={
                    "registration": "x",
                    "vin": "x",
                    "first_registration_date": "x"
                })

                assert response.status_code == 400
                assert response.get_json() == {'error': 'Invalid car details'}
        """
        mocker.patch.object(CepikSevice, '__init__', lambda *args, **kwargs: Exception())
        response = client.get('/car_status', json={
            "registration": "x",
            "vin": "x",
            "first_registration_date": "x"
        })

        assert response.status_code == 400
        assert response.get_json() == {'error': 'Invalid car details'}


class TestWithFullReportUrlRoute:
    """
    TestWithFullReportUrlRoute

    This class contains unit tests for the TestWithFullReportUrlRoute route.

    Methods:
    - test_car_status_successful_response
    - test_car_status_with_unsuccessful_response
    """
    def test_car_status_successful_response(self, client, mocker) -> None:
        """
        Test Car Status Successful Response

        This method tests the successful response of retrieving car status.

        :param client: The client used for sending HTTP requests.
        :param mocker: The mocker object used for patching methods.
        :return: None
        """
        car_details = {
            "registration": "DPL29742",
            "vin": "WVWZZZ3CZ6E101738",
            "first_registration_date": "23.03.2006"
        }
        mocker.patch.object(CepikSevice, '__init__', lambda *args, **kwargs: None)
        mocker.patch.object(CepikSevice, 'get_full_vehicle_history_report_url', lambda *args, **kwargs: 'http://localhost')

        response = client.get('/with_full_report_url', json=car_details)
        assert response.status_code == 200
        assert response.get_json() == {**car_details, 'full_report_url': 'http://localhost'}

    def test_car_status_with_unsuccessful_response(self, client, mocker) -> None:
        """
        :param client: Flask test client object used for making API requests
        :param mocker: Mock object used for patching the CepikService __init__ method
        :return: None

        This method is used to test the car_status endpoint when the API response is unsuccessful. It takes in a Flask test client object and a mocker object as parameters.

        The method starts by patching the CepikSevice __init__ method with a lambda function that always raises an Exception. This is done to simulate an error condition during the initialization
        * of the CepikService.

        Then, a GET request is made to the '/car_status' endpoint of the client with a JSON payload containing car details.

        After making the request, the method asserts that the response status code is 400, indicating a bad request, and that the response JSON matches the expected error message {'error': '
        *Invalid car details'}.
        """
        mocker.patch.object(CepikSevice, '__init__', lambda *args, **kwargs: Exception())
        response = client.get('/car_status', json={
            "registration": "x",
            "vin": "x",
            "first_registration_date": "x"
        })

        assert response.status_code == 400
        assert response.get_json() == {'error': 'Invalid car details'}
