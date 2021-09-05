import os.path

import allure
import pytest
from allure_commons.types import AttachmentType

from models.personal_data import PersonalData as PD

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


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

        app.authentication_page.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Successful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert app.personal_data.is_changed(), "Personal data is not changed!"

    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(
        self, app, authorize, field
    ):
        """
        Steps
        1. Open main page
        2. Authenticate with valid data
        3. Check authenticate result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successful
        """

        app.authentication_page.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Unsuccessful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize(
        "name, last_name",
        [
            ["123", "123"],
            ["---", "---"],
            ["\xbdR6\x10\x7f", "\xbdR6\x10\x7f"],
            [PD().random().url, PD().random().url],
            [PD().random().image_url, PD().random().image_url],
        ],
    )
    @pytest.mark.xfail
    @pytest.mark.bug
    def test_edit_incorrect_name_lastname(self, app, authorize, name, last_name):
        """
        Steps
        1. Open authentication page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit name or(and) lastname as digits
        6. Check editing is not successfully
        """
        app.authentication_page.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Unsuccessful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.set_user_image
    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_set_user_image(self, app, authorize, image_file):
        """
        Steps
        1. Open main page
        2. Authenticate with valid data
        3. Check authenticate result
        4. Go to page with editing personal data
        5. Edit user image
        6. Check successful editing
        """
        app.authentication_page.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.set_user_image(
            image_file, personal_data.user_image_description
        )
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Successful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert app.personal_data.is_user_image_changed(), "User image not changed!"
