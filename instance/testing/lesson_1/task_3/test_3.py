from subprocess import Popen, PIPE


def get_result():
    result = "Человек: Ауууу!\nЭхо: Ауууу!"
    command = "python ./instance/testing/lesson_1/task_3/test_file_3.py"
    p = Popen(command, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate()
    return out.strip() == result


if __name__ == "__main__":
    print(get_result())
