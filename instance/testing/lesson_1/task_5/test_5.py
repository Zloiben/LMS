from subprocess import Popen, PIPE

# input, result
test_variants = [
    ("print", "print ? Конечно, помню, ведь мы проходили это на прошлом занятии!")
]


def testing(input_data: str, result_waiting: str) -> tuple:
    """
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :param result_waiting: ожидаемый результат.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_1/task_5/test_file_5.py"
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    print(err)
    return out.strip() == result_waiting, out.strip()


def get_result():
    data_testing = []
    for index, test in enumerate(test_variants):
        result_testing = testing(test[0], test[1])
        print(result_testing)
        if result_testing[0] is False:
            return index, result_testing
        data_testing.append(result_testing[0])
    if all(data_testing):
        return True
    return False
