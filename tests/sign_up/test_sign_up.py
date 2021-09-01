from models.authenticate import AuthenticationData
from models.sign_up import SignUpData


class TestSignUp:
    def test_valid_sign_up_data(self, app):
        """
        Steps
        1. Open Authentication page
        2. Click the "Создать учетную запись" button
        3. Fill in the required fields: Login, Password, Email (with mask test@test.te), Email one more time,
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
