from subprocess import Popen, PIPE

# input, result
test_variants = [
    ("", "ДА"),
    ("Hi\nCarramba!\nHohoho", "НЕТ"),
    ("Карамба!\nКоррида!\nЧерт подери!", "НЕТ")
]


def testing(input_data: str, result_waiting: str) -> tuple:
    """
    # Условие оператор Дзен
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :param result_waiting: ожидаемый результат.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    COMMAND = r"python ./instance/testing/lesson_2/task_10/test_file_10.py"
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
