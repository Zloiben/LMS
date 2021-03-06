from subprocess import Popen, PIPE


def function(input_data: str):
    n = int(input_data)
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    return str(count)


# input, result
test_variants = [
    "10",
    "15",
    "20",
    "99",
    "100",
    "199",
    "119"
]


def testing(input_data: str) -> tuple:
    """
    # цикл while Сколько строк?
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :return Возвращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_4/task_20/test_file_20.py"
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


if __name__ == "__main__":
    print(get_result())