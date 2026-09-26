from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class PasswordAuthentication(Authentication):
    def login(self):
        print("Login using Password")


class OTPAuthentication(Authentication):
    def login(self):
        print("Login using OTP")


class BiometricAuthentication(Authentication):
    def login(self):
        print("Login using Biometric")


methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.login()