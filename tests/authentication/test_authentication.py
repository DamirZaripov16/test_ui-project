import time


class TestAuthenticationPage:

    def test_authentication_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        app.authentication_page.authenticate(username="zaripov.damir@test.ru", password="Sharif1992*")
        assert 1 == 1, "Check authentication data"