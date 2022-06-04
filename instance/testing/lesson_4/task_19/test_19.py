from subprocess import Popen, PIPE


# input, result
test_variants = [
    ("22.3\n24.1\n24.0\n24.4\n-301", "23.7")
]


def testing(input_data: str, wait_result: str) -> tuple:
    """
    # цикл while Сколько строк?
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :return Возвращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_4/task_19/test_file_19.py"
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip()[:4] == wait_result, out.strip()


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