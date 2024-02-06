from app.db.configuration import sa
from typing import Self
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(sa.Model):
    """

    The UserModel class represents a user in the system. It extends the sa.Model class.

    Attributes:
    - id: An integer representing the primary key of the user.
    - username: A string representing the username of the user.
    - password: A string representing the hashed password of the user.
    - email: A string representing the email address of the user.
    - role: A string representing the role of the user.
    - active: A boolean indicating the activity status of the user.

    Methods:
    - __init__(self, username: str, password: str, email: str, role: str):
        Initializes a new instance of the UserModel class with the specified attributes.
    - save_or_update(self) -> None:
        Saves or updates the user in the database.
    - check_password(self, password: str) -> bool:
        Checks if the provided password matches the stored hashed password for the user.
    - as_dict(self):
        Returns a dictionary representation of the user, containing username, role, and active status.
    - find_by_username(cls, username: str) -> Self | None:
        Finds and returns the user with the specified username, or None if not found.
    - find_by_email(cls, email: str) -> Self | None:
        Finds and returns the user with the specified email address, or None if not found.
    - find_by_id(cls, id_: int) -> Self | None:
        Finds and returns the user with the specified ID, or None if not found.

    """
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(255))
    password = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))
    role = sa.Column(sa.String(10), default="USER")
    active = sa.Column(sa.Boolean, default=False)

    def __init__(self, username: str, password: str, email: str, role: str = "USER"):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.role = role

    def save_or_update(self) -> None:
        """
        Save or update the current object in the database.
        @return: None
        """
        sa.session.add(self)
        sa.session.commit()

    def check_password(self, password: str) -> bool:
        """
        @param password: The password to be checked against the stored hash.
        @return: True if the password matches the stored hash, False otherwise.
        """
        return check_password_hash(self.password, password)

    def as_dict(self):
        """
        @return: A dictionary representation of the object with the following keys:
            - 'username': The username of the user.
            - 'role': The role of the user.
            - 'active': The status of the user.
        """
        return {
            'username': self.username,
            'role': self.role,
            'active': self.active
        }

    def is_activated(self) -> bool:
        return self.active

    @classmethod
    def find_by_username(cls, username: str) -> Self | None:
        """
        Find a user by their username.

        @param username: The username of the user to find.
        @return: The user object if found, otherwise None.
        """
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> Self | None:
        """
        Find a user by email.

        @param email: The email address to search for.
        @return: The user with the specified email, or None if no user is found.
        """
        return UserModel.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id_: int) -> Self | None:
        """
        @param id_: The id of the user to search for.
        @return: The user object with the specified id if found, otherwise None.
        """
        return UserModel.query.filter_by(id=id_).first()
