import pytest

from common.constants import PersonalDataConstants


class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app, authorize):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successful editing
        """

        if not app.authentication_page.is_authorized():
            assert app.authentication_page.is_authorized(), "We are not logged in!"
        app.authentication_page.go_to_editing_personal_data()
        app.personal_data.edit_personal_data()
        assert app.personal_data.is_changed(), "Personal data is not changed!"
        assert (
            PersonalDataConstants.SUCCESSFULLY_CHANGED_MESSAGE
            == app.personal_data.successfully_changed_check()
        ), "Changes are not applied"

    @pytest.mark.parametrize(
        "data",
        [
            {"name": "", "lastname": "", "email": ""},
            {"name": "", "lastname": "Зарипов", "email": "test@test.ru"},
            {"name": "Дамир", "lastname": "", "email": "test@test.ru"},
            {"name": "Дамир", "lastname": "Зарипов", "email": ""},
            {"name": "Дамир", "lastname": "Зарипов", "email": "testtest.ru"},
            {"name": "Дамир", "lastname": "Зарипов", "email": "@test.ru"},
        ],
    )
    def test_invalid_edit_basic_personal_data(self, app, data, authorize):
        """
        Steps
        1. Open main page
        2. Authenticate with valid data
        3. Check authenticate result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successful
        """

        if not app.authentication_page.is_authorized():
            assert app.authentication_page.is_authorized(), "We are not logged in!"
        app.authentication_page.go_to_editing_personal_data()
        app.personal_data.edit_personal_data(**data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"
