from subprocess import Popen, PIPE


def get_result():
    result = "1 бит - минимальная единица количества информации.\n1 байт = 8 бит.\n1 Килобит = 1024 бита.\n" \
             "1 Килобайт = 1024 байта.\n1 Килобайт = 8192 бит."
    command = "python ./instance/testing/lesson_1/task_4/test_file_4.py"
    p = Popen(command, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate()
    return out.strip() == result.strip()


if __name__ == "__main__":
    print(get_result())
