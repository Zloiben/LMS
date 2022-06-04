import re

# -------------------------------------------Настройки приложения-------------------------------------------------------


# путь для загрузки фалов для тестов
UPLOAD_FOLDER = f'instance\\testing'

# -------------------------------------------Для проверки---------------------------------------------------------------


# Для проверки почты.
REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Для проверки файла.
ALLOWED_EXTENSIONS = ['py', 'txt']

# --------------------------------------------Пользователь--------------------------------------------------------------

# Админ роли
ADMIN_ROLES = ["SuperAdmin", "Moderator"]
# Все роли
ALL_ROLES = ["SuperAdmin", "Moderator", "Teacher", "User"]

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
                        "max_score": 15
                    },
                    "task_4": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    },
                    "task_5": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    }
                },
                "2": {
                    "task_6": {
                        "result": "-",
                        "score": 0,
                        "max_score": 14
                    },
                    "task_7": {
                        "result": "-",
                        "score": 0,
                        "max_score": 20
                    },
                    "task_8": {
                        "result": "-",
                        "score": 0,
                        "max_score": 15
                    },
                    "task_9": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    },
                    "task_10": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    }
                },
                "3": {
                    "task_11": {
                        "result": "-",
                        "score": 0,
                        "max_score": 14
                    },
                    "task_12": {
                        "result": "-",
                        "score": 0,
                        "max_score": 20
                    },
                    "task_13": {
                        "result": "-",
                        "score": 0,
                        "max_score": 15
                    },
                    "task_14": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    },
                    "task_15": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    }
                }
                , "4": {
                    "task_16": {
                        "result": "-",
                        "score": 0,
                        "max_score": 14
                    },
                    "task_17": {
                        "result": "-",
                        "score": 0,
                        "max_score": 20
                    },
                    "task_18": {
                        "result": "-",
                        "score": 0,
                        "max_score": 15
                    },
                    "task_19": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    },
                    "task_20": {
                        "result": "-",
                        "score": 0,
                        "max_score": 30
                    }
                }
            }
        }
    }
}

# ---------------------------------------------API keys ----------------------------------------------------------------

API_KEYS = {
    "APP_KEY": 'yandexlyceum_secret_key',
    "YANDEX_DISK": "AQAAAAAd17NAAAf0e4Aj2TYlp0Ydi9zf6K2Gsis"
}
