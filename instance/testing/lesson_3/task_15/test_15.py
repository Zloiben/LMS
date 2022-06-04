from subprocess import Popen, PIPE


def function(input_data) -> str:
    a = int(input_data)
    if a % 4 == 0 and a % 100 != 0:
        result = 'Високосный'
    elif a % 400 == 0:
        result = 'Високосный'
    else:
        result = 'Не високосный'

    return str(result)


# input, result
test_variants = [
    "2016",
    "1900",
    "1000",
    "1223",
    "1231",
    "2022",
    "2021",
    "2020",
    "2019",
    "2018",
    "2017",
    "2000"
]


def testing(input_data: str) -> tuple:
    """
    # Простые функции Високосный
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_3/task_15/test_file_15.py"
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    result = function(input_data)
    return out.strip() == result, out.strip(), result


def get_result():
    data_testing = []
    for index, test in enumerate(test_variants):
        result_testing = testing(test)
        if result_testing[0] is False:
            return index, result_testing[1], test, result_testing[2]
        data_testing.append(result_testing[0])
    if all(data_testing):
        return True
    return False
