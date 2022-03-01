from subprocess import Popen, PIPE
COMMAND = r"python ./instance/testing/lesson_1/task_2/test_file_2.py"


def test_1(input_data, result):
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == result


def test_2(input_data, result):
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == result


def test_3(input_data, result):
    p = Popen(COMMAND, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate(input=input_data)
    return out.strip() == result


def get_result():
    """Ответ Hello, World!"""
    if test_1("3\n2\n1", "1\n2\n3"):
        if test_2("Hi\nCarramba!\nHohoho", "Hohoho\nCarramba!\nHi"):
            if test_3("Карамба!\nКоррида!\nЧерт подери!", "Черт подери!\nКоррида!\nКарамба!"):
                return True
    return False
