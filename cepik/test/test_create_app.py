from flask import Flask

from app.create_app import main


def test_create_app() -> object:
    """
    Test the `create_app` method.

    :return: The created Flask app object.
    """
    test_app = main()

    with test_app.test_client():
        assert test_app is not None
        assert isinstance(test_app, Flask)

