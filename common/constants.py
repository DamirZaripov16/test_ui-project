class AuthenticationConstants:
    AUTHENTICATION_ERROR = "Неверный логин или пароль, попробуйте заново."


class SignUpConstants:
    SIGN_UP_PAGE_URL = "https://qacoursemoodle.innopolis.university/login/signup.php?"


class PersonalDataConstants:
    EMAIL_DISPLAY_MODES = {
        "hidden": "0",
        "all_can_see": "1",
        "show_to_course_participants": "2",
    }
    TIMEZONE_VALUES = (
        "99",
        "Asia/Dubai",
        "America/Santiago",
        "Africa/Tunis",
        "Europe/Moscow",
        "Europe/Moscow",
        "UTC",
    )


class AccountConstants:
    ADMINISTRATION = "Администрирование"
    COURSES = "Курсы"
    CREATE_COURSE = "Добавить курс"


class CourseConstants:
    DELETED_COURSE = "был полностью удален"
    FULLNAME_ERROR = "- Заполните поле"
    SHORTNAME_ERROR = "- Не указано краткое название"


class CreateCourseConstants:
    SECTION_NUMBER = 52
    COURSE_LANGUAGE = "ru"
    CURRENT_YEAR = 2021
    LAST_YEAR = 2050
    FILE_SIZES_VALUES = [
        0,
        2097152,
        1048576,
        512000,
        102400,
        51200,
        10240,
    ]
