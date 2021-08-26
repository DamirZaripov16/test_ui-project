from faker import Faker

fake = Faker("Ru-ru")


class AuthenticationData:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return AuthenticationData(username, password)
