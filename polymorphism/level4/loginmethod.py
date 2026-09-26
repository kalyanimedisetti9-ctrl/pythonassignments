class GoogleLogin:
    def login(self):
        print("Logged in using Google")

class FacebookLogin:
    def login(self):
        print("Logged in using Facebook")

class EmailLogin:
    def login(self):
        print("Logged in using Email")


def authenticate(user):
    user.login()


authenticate(GoogleLogin())
authenticate(FacebookLogin())
authenticate(EmailLogin())