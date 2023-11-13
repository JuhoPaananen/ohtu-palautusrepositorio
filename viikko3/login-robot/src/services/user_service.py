from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository
        self._username_pattern = "^[a-z]{3,}$"
        self._password_pattern = "^(?=.*[^a-zA-Z]).{8,}$"

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not re.match(self._username_pattern, username):
            raise UserInputError("Invalid username, at least 3 characters and only a-z allowed")

        if not re.match(self._password_pattern, password):
            raise UserInputError("Invalid password, at least 8 characters and one special character required")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists")
