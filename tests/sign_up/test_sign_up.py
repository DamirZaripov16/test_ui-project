import pytest

from models.authenticate import AuthenticationData
from models.sign_up import SignUpData


class TestSignUp:
    def test_valid_sign_up_data(self, app):
        """
        Steps
        1. Open Authentication page
        2. Click the "Создать учетную запись" button
        3. Fill in the required fields: Login, Password,
        Email (with mask test@test.te), Email one more time,
        Firstname, Second name
        6. Click the "Создать мой новый аккаунт" button
        7. Search "Отправить вам письмо не удалось!" text
        7.1 Check
        8. Click "Продолжить" button
        9. __Login with the entered data__
        9.1 Check
        10. Search "Необходимо подтвердить учетную запись" text
        10.1 Check
        """
        app.open_authentication_page()
        app.authentication_page.go_to_sign_up_page()
        data = SignUpData().random()
        app.sign_up_page.sign_up(data)
        assert app.sign_up_page.check_account_create(), "We are not logged in!"
        app.sign_up_page.click_continue()
        app.sign_up_page.click_log_in()
        authenticate_data = AuthenticationData(data.login, data.password)
        app.authentication_page.authorize(authenticate_data)
        assert app.sign_up_page.check_new_account_log_in(), "We are not logged in!"

    @pytest.mark.parametrize(
        "field", ["login", "password", "email", "first_name", "last_name"]
    )
    def test_invalid_sign_up_data(self, app, field):
        """
        Steps
        1. Open Login page
        2. Click the "Создать учетную запись" button
        3. Fill in the required fields: Login, Password,
        Email (with mask test@test.te), Email one more time,
        Firstname, Second name
        4. Click the "Создать мой новый аккаунт" button
        5. Checking for registration of a new user without empty required fields
        """

        app.open_authentication_page()
        app.authentication_page.go_to_sign_up_page()
        data = SignUpData().random()
        setattr(data, field, None)
        app.sign_up_page.sign_up(data)
        assert (
            not app.sign_up_page.is_signed_up()
        ), "We are sign up with empty required fields!"
