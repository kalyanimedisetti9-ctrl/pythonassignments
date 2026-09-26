class InvalidUsernameError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

class DuplicateUsernameError(Exception):
    pass

class InvalidLoginError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        try:
            if len(username) < 3:
                raise InvalidUsernameError("Username must have at least 3 characters")

            if username in self.users:
                raise DuplicateUsernameError("Username already exists")

            if len(password) < 8:
                raise WeakPasswordError("Password must have at least 8 characters")

            self.users[username] = password
            print("Registration successful")

        except InvalidUsernameError as e:
            print("Error:", e)
        except DuplicateUsernameError as e:
            print("Error:", e)
        except WeakPasswordError as e:
            print("Error:", e)

    def login(self, username, password):
        try:
            if username not in self.users:
                raise InvalidLoginError("Invalid username or password")

            if self.users[username] != password:
                raise InvalidLoginError("Invalid username or password")

            print("Login successful")

        except InvalidLoginError as e:
            print("Error:", e)


system = LoginSystem()

system.register("kalyani", "python123")
system.register("kalyani", "java12345")
system.register("ab", "python123")

system.login("kalyani", "python123")
system.login("kalyani", "wrong123")