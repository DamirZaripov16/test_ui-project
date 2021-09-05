import pytest

from common.constants import AuthenticationConstants
from models.authenticate import AuthenticationData


class TestAuthenticationPage:
    def test_authentication_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Authenticate with valid data
        3. Check authentication result
        """
        app.open_authentication_page()
        data = AuthenticationData(
            username="zaripov.damir@test.ru", password="Sharif1992*"
        )
        app.authentication_page.authorize(data)
        assert app.authentication_page.is_authorized(), "We are not logged in!"
        # app.authentication_page.log_out()

    def test_authentication_invalid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Authenticate with invalid data
        3. Check authentication result
        """
        app.open_authentication_page()
        data = AuthenticationData.random()
        app.authentication_page.authorize(data)
        assert (
            AuthenticationConstants.AUTHENTICATION_ERROR
            == app.authentication_page.authentication_login_error()
        ), "We are logged in!"

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_authentication_empty_data(self, app, field):
        """
        Steps
        1. Open main page
        2. Authenticate with empty data
        3. Check authenticate result
        """
        app.open_authentication_page()
        data = AuthenticationData.random()
        setattr(data, field, None)
        app.authentication_page.authorize(data)
        assert (
            AuthenticationConstants.AUTHENTICATION_ERROR
            == app.authentication_page.authentication_login_error()
        ), "We are logged in!"
