import re


# -------------------------------------------Настройки приложения-------------------------------------------------------


# путь для загрузки фалов для тестов
UPLOAD_FOLDER = f'instance\\testing'


# -------------------------------------------Для проверки---------------------------------------------------------------


# Для проверки почты. file - checking.py function - check_email
REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Для проверки файла. file - checking.py function - allowed_file
ALLOWED_EXTENSIONS = ['py', 'txt']


# --------------------------------------------Пользователь--------------------------------------------------------------


standard_data = {
    "courses": {
        "Python Basics": {
            "profile": {
                "all_score": 0
            },
            "lessons": {
                "1": {
                    "task_1": {
                        "result": "-",
                        "score": 0,
                        "max_score": 14
                    },
                    "task_2": {
                        "result": "-",
                        "score": 0,
                        "max_score": 20
                    },
                    "task_3": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    }
                }
            }
        }
    }
}
