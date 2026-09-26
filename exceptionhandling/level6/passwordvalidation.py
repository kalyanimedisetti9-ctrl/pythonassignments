class InvalidPasswordError(Exception):
    pass


def validate_password(password):
    try:
        if len(password) < 8:
            raise InvalidPasswordError("Password must contain at least 8 characters")
        print("Valid password")
    except InvalidPasswordError as e:
        print("Error:", e)

validate_password("Python123")
validate_password("abc")