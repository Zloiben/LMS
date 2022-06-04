from subprocess import Popen, PIPE

# input, result
test_variants = [
    ("S.L.Jackson\nMEGAKILLER@example.com", "OK"),
    ("@@@\noops", "Некорректный логин"),
    ("ofxkj\ngjgzxcf", "Некорректный адрес"),
    ("@\n@", "Некорректный логин"),
    ("@\ngjgzxcf", "Некорректный логин")
]


def testing(input_data: str, result_waiting: str) -> tuple:
    """
    # Условный оператор Регистрация почты
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :param result_waiting: ожидаемый результат.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_2/task_8/test_file_8.py"
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == result_waiting, out.strip()


def get_result():
    data_testing = []
    for index, test in enumerate(test_variants):
        result_testing = testing(test[0], test[1])
        if result_testing[0] is False:
            return index, result_testing[1], test[0], test[1]
        data_testing.append(result_testing[0])
    if all(data_testing):
        return True
    return False


if __name__ == "__main__":
    print(get_result())
