from flask import Flask

from app.create_app import main


def test_create_app(sqlalchemy_database_uri: object) -> object:
    """
    :param sqlalchemy_database_uri: The SQLAlchemy database URI to use for creating the test Flask application.
    :return: The test Flask application object.

    This method is used to test the `create_app` function by asserting various conditions on the test Flask application object. It creates a test Flask application using the `main` function
    * and performs the following assertions:
    1. Asserts that the test Flask application object is not None.
    2. Asserts that the test Flask application object is an instance of the Flask class.
    3. Asserts that the SQLAlchemy database URI configuration property of the test Flask application matches the provided `sqlalchemy_database_uri` parameter.
    4. Asserts that the SQLALCHEMY_TRACK_MODIFICATIONS configuration property of the test Flask application is set to False.

    Note: This method does not return anything, as the purpose is to perform the assertions and verify the behavior of the `create_app` function.
    """
    test_app = main()

    with test_app.test_client():
        assert test_app is not None
        assert isinstance(test_app, Flask)
        assert test_app.config['SQLALCHEMY_DATABASE_URI'] == sqlalchemy_database_uri
        assert test_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
