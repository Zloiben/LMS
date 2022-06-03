from subprocess import Popen, PIPE


def function(input_data) -> str:
    a = int(input_data)
    if ((a // 100) + (a % 10)) / 2 == ((a // 10) % 10):
        result = 'Вы ввели красивое число'
    elif ((a // 100) + ((a // 10) % 10)) / 2 == (a % 10):
        result = 'Вы ввели красивое число'
    elif ((a % 10) + ((a // 10) % 10)) / 2 == (a // 100):
        result = 'Вы ввели красивое число'
    else:
        result = 'Жаль, вы ввели обычное число'

    return str(result)


# input, result
test_variants = [
    "9",
    "1233",
    "1231",
    "-221",
    "612",
    "10",
    "0",
    "135",
    "468",
    "884",
    "122223332",
    "1233131231312312"
]


def testing(input_data: str) -> tuple:
    """
    # Простые функции Красивое число
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_3/task_4/test_file_4.py"
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == function(input_data), out.strip()


def get_result():
    data_testing = []
    for index, test in enumerate(test_variants):
        result_testing = testing(test[0])
        if result_testing[0] is False:
            return index, result_testing[1], test[0], test[1]
        data_testing.append(result_testing[0])
    if all(data_testing):
        return True
    return False
