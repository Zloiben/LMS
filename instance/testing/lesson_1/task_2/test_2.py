from subprocess import Popen, PIPE

COMMAND = r"python ./test_file_2.py"

# input, result
test_variants = [
    ("3\n2\n1", "1\n2\n3"),
    ("Hi\nCarramba!\nHohoho", "Hohoho\nCarramba!\nHi"),
    ("Карамба!\nКоррида!\nЧерт подери!", "Черт подери!\nКоррида!\nКарамба!")
]


def testing(input_data: str, result_waiting: str) -> tuple:
    """
    функция для тестирования отправленных файлов.
    :param input_data: вводимые данные.
    :param result_waiting: ожидаемый результат.
    :return Возращает кортеж (Результат, что было выведенною)
    """
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == result_waiting, out.strip()


def get_result():
    """Ответ Hello, World!"""
    data_testing = []
    for index, test in enumerate(test_variants):
        result_testing = testing(test[0], test[1])
        data_testing.append(result_testing[0])
        # TODO: Пока что сдеалл чтобы просто возращало True или False
        #   В будущем trello Переделать тесты
    if all(data_testing):
        return True
    return False
