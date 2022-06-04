from subprocess import Popen, PIPE


def function(input_data: str) -> str:
    n = int(input_data)
    while n % 8 != n:
        n //= 8
    return str(n)


# input, result
test_variants = [
    "129",
    "333",
    "12313",
    "343543543",
    "1",
    "2",
    "3",
    "5",
    "20",
    "50",
    "60"
]


def testing(input_data: str) -> tuple:
    """
    # цикл while Учитель
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :return Возвращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_3/task_17/test_file_17.py"
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
