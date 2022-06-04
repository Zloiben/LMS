from subprocess import Popen, PIPE


def get_result():
    # Простые функции Факториал: первое знакомство
    result = str(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)

    command = r"python ./instance/testing/lesson_3/task_11/test_file_11.py"
    p = Popen(command, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate()
    return out.strip() == result


if __name__ == "__main__":
    print(get_result())
