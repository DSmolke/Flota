from rest_framework import status
from rest_framework.views import APIView, Response, Request
from drivers.models import DriverModel
from drivers.serailizers import DriverModelSerializer, DriverSerializer
class AllDriversResource(APIView):
    """

    Class: AllDriversResource

    This class is responsible for handling the API endpoint to retrieve all drivers.

    Methods:
    1. get(request: Request) -> Response
       - Description: Retrieves all drivers from the database and returns the serialized data.
       - Parameters:
           - request (Request): The HTTP request object.
       - Returns:
           - Response: The HTTP response object containing the serialized data.

    """
    def get(self, request: Request) -> Response:
        """

        Parameters:
        - request (Request): The request object containing the client's request data.

        Return:
        - Response: The response object containing the serialized data of all driver models in the database.

        Description:
        This method retrieves all driver models from the database and serializes them using the DriverModelSerializer.
        The serialized data is then returned as a Response object with HTTP status code 200 (OK).

        """
        drivers = DriverModel.objects.all()
        serializer = DriverModelSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddDriverResource(APIView):
    """
    Class: AddDriverResource

    Class Description:
        This class is responsible for handling HTTP POST requests to add a new driver.

    Methods:
        - post(request: Request) -> Response
            This method handles the POST request and saves the driver details if the provided data is valid.
            It returns a Response object with the appropriate status and data.

    Parameters:
        - request (Request): The HTTP request object containing the driver details.

    Returns:
        - Response: The HTTP response object with the serialized data or error messages.

    Exceptions:
        None

    Example Usage:
        # Create an instance of the AddDriverResource class
        add_driver_resource = AddDriverResource()

        # Make a POST request to add a new driver
        request = Request(...)
        response = add_driver_resource.post(request)
    """
    def post(self, request: Request) -> Response:
        """
        Post Method

        This method is responsible for creating a new instance of a driver using the provided request data.

        Parameters:
        - request: An instance of the Request class. It contains the data needed to create the new driver instance.

        Return:
        - An instance of the Response class. It either contains the serialized data of the newly created driver instance along with a status code of 201 (HTTP_CREATED) if the serializer is valid
        *, or the serializer errors along with a status code of 400 (HTTP_BAD_REQUEST) if the serializer is invalid.

        Example Usage:
        ```
        request = Request(data=<data>)
        response = post(request)
        print(response.data)
        print(response.status_code)
        ```
        """
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriversResource(APIView):
    """
    Class for handling API requests related to drivers.

    Methods:
    - get: Get information about a specific driver.
    - delete: Delete a specific driver.
    - patch: Update information of a specific driver.

    """
    def get(self, request: Request, driver_id: int) -> Response:
        """
        Get a driver by ID.

        Parameters:
            request (Request): The HTTP request object.
            driver_id (int): The ID of the driver to retrieve.

        Returns:
            Response: The HTTP response containing the serialized driver data.

        Raises:
            DriverModel.DoesNotExist: If the driver with the specified ID does not exist.
        """
        try:
            driver = DriverModel.objects.get(pk=driver_id)
            serializer = DriverSerializer(driver)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DriverModel.DoesNotExist:
            return Response({"message": "Driver does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, driver_id: int) -> Response:
        """
        Delete a driver by driver ID.

        Parameters:
            - request (Request): The HTTP request object.
            - driver_id (int): The ID of the driver to be deleted.

        Returns:
            - Response: The HTTP response object indicating the status of the delete operation.

        """
        try:
            driver_to_delete = DriverModel.objects.get(pk=driver_id)
            driver_to_delete.delete()
            return Response({"message": "Driver has been deleted"}, status=status.HTTP_200_OK)
        except DriverModel.DoesNotExist:
            return Response({"message": "Driver not found"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, driver_id: int) -> Response:
        """
        Updates the driver information.

        Parameters:
        - request (Request): The HTTP request object.
        - driver_id (int): The ID of the driver to be updated.

        Returns:
        - Response: The HTTP response object containing the updated driver information if successful (status code 200).
        - Response: The HTTP response object with an error message if the request is invalid (status code 400).
        - Response: The HTTP response object with an error message if the specified driver does not exist (status code 400).
        """
        try:
            driver_to_update = DriverModel.objects.get(pk=driver_id)
            serializer = DriverSerializer(driver_to_update, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        except DriverModel.DoesNotExist:
            return Response({"message": "Driver does not exist"}, status=status.HTTP_400_BAD_REQUEST)
