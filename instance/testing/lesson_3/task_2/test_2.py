from subprocess import Popen, PIPE


def get_result():
    # Простые функции Количество минут в году
    days_per_year = 365
    hours_per_day = 24
    minutes_per_hour = 60

    result = str(minutes_per_hour * hours_per_day * days_per_year)

    command = r"python ./instance/testing/lesson_3/task_2/test_file_2.py"
    p = Popen(command, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate()
    return out.strip() == result


if __name__ == "__main__":
    print(get_result())
