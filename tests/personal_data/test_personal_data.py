import pytest

from models.authenticate import AuthenticationData


class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successful editing
        """
        app.open_main_page()
        if not app.authentication_page.is_authorized():
            app.open_authentication_page()
            data = AuthenticationData(username="zaripov.damir@test.ru", password="Sharif1992*")
            app.authentication_page.authorize(data)
            assert app.authentication_page.is_authorized(), "We are not logged in!"
        app.authentication_page.go_to_editing_personal_data()
        app.personal_data.edit_personal_data()
        assert app.personal_data.is_changed(), "Personal data is not changed!"

    @pytest.mark.parametrize(
        "data",
        [
            {"name": "", "lastname": "", "email": ""},
            {"name": "", "lastname": "Зарипов", "email": "test@test.ru"},
            {"name": "Дамир", "lastname": "", "email": "test@test.ru"},
            {"name": "Дамир", "lastname": "Зарипов", "email": ""},
            {"name": "Дамир", "lastname": "Зарипов", "email": "test@test.ru"},
            {"name": "Дамир", "lastname": "Зарипов", "email": "@test.ru"},
        ],
    )
    def test_invalid_edit_basic_personal_data(self, app, data):
        """
        Steps
        1. Open main page
        2. Authenticate with valid data
        3. Check authenticate result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successful
        """
        app.open_main_page()
        if not app.authentication_page.is_authorized():
            app.open_authentication_page()
            other_data = AuthenticationData(username="zaripov.damir@test.ru", password="Sharif1992*")
            app.authentication_page.authorize(other_data)
            assert app.authentication_page.is_authorized(), "We are not logged in!"
        app.authentication_page.go_to_editing_personal_data()
        app.personal_data.edit_personal_data(**data)
        assert not app.personal_data.is_changed(), "Personal data should not be changed!"
