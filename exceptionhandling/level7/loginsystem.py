class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.username = "admin"
        self.password = "12345"

    def login(self, username, password):
        try:
            if username != self.username:
                raise InvalidUsernameError("Invalid username")

            if password != self.password:
                raise InvalidPasswordError("Invalid password")

            print("Login successful")

        except InvalidUsernameError as e:
            print("Error:", e)
        except InvalidPasswordError as e:
            print("Error:", e)


login = LoginSystem()
login.login("admin", "12345")
login.login("user", "12345")
login.login("admin", "wrong")