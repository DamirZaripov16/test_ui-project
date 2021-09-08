import pytest

from common.constants import CourseConstants
from models.create_course import CreateCourse


class TestCourseCreation:
    def test_valid_course_creation(self, app, authorize):
        """
        Steps
        1. Authorize with admin credentials.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Fill the «Полное название курса»,
        «Краткое название курса» fields.
        4. Enter day, month, year and time for course end date field.
        5. Fill the «Дата окончания курса»,
        «Описание» fields in "Общие" section.
        6. Choose the number in «Количество секций» field
        in "Формат курса" section.
        7. By the «Принудительный язык» dropdown
        choose the Russian language in "Внешний вид" section
        8. By the «Максимальный размер загружаемого файла» dropdown
        choose the desired value in "Файлы и загрузки" section
        9. Fill the following fields:
            «Ваше слово вместо «Управляющий»»,
             «Ваше слово вместо «Учитель»»,
             «Ваше слово вместо «Студент»».
             in "Переименование Ролей" section
        10. Click the «Сохранить и показать» button.
        11. Click the «Перейти к курсу» button.
        12. Check if the created course name is in the page header.
        13. Go to https://qacoursemoodle.innopolis.university/course/index.php.
        14. Click the «Управление курсами» button.
        15. Find the created course name on the page.
        16. Click the delete button next to the new course name.
        17. Confirm deletion by clicking «Удалить» button.
        18. Check the "{the new course name} был полностью удален" text.
        """
        app.open_main_page()
        app.authentication_page.go_to_administration_page()
        app.authentication_page.go_to_course_page()
        app.authentication_page.go_to_create_course_page()
        course_info = CreateCourse.random()
        app.create_course.create_course(course_info)
        assert (
            app.create_course.new_course_page() == course_info.full_course_name
        ), "The course was not created!"
        app.open_course_page()
        app.course.go_to_manage_courses()
        app.course.find_course_full_name(course_info.full_course_name)
        app.course.delete_course()
        app.course.confirm_delete()
        delete_confirmation = (
            f"{course_info.short_course_name} {CourseConstants.DELETED_COURSE}"
        )
        assert (
            app.course.find_delete_confirmation() == delete_confirmation
        ), "The course was not deleted!"

    @pytest.mark.parametrize("field", ["full_course_name"])
    def test_invalid_course_creation_no_full_name(self, app, field, authorize):
        """
        Steps
        1. Authorize with admin credentials.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Do not fill the required «Полное название курса» field.
        4. Fill the «Краткое название курса» field.
        5. Click the «Сохранить и показать» button.
        6. Check the "- Заполните поле" text.
        """
        app.open_main_page()
        app.authentication_page.go_to_administration_page()
        app.authentication_page.go_to_course_page()
        app.authentication_page.go_to_create_course_page()
        course_info = CreateCourse.random()
        setattr(course_info, field, None)
        app.create_course.create_course(course_info)
        assert (
            app.course.find_fullname_error() == CourseConstants.FULLNAME_ERROR
        ), "The course was created without fullname!"

    @pytest.mark.parametrize("field", ["short_course_name"])
    def test_invalid_course_creation_no_short_name(self, app, field, authorize):
        """
        Steps
        1. Authorize with admin credentials.
        2. Go to Administration page.
        3. Go to Courses tab.
        4. Go to Create Course page.
        3. Fill the «Полное название курса» field.
        4. Do not fill the required «Краткое название курса» field.
        5. Click the «Сохранить и показать» button.
        6. Check the "- Не указано краткое название" text.
        """
        app.open_main_page()
        app.authentication_page.go_to_administration_page()
        app.authentication_page.go_to_course_page()
        app.authentication_page.go_to_create_course_page()
        course_info = CreateCourse.random()
        setattr(course_info, field, None)
        app.create_course.create_course(course_info)
        assert (
            app.course.find_shortname_error() == CourseConstants.SHORTNAME_ERROR
        ), "The course was created without shortname!"
