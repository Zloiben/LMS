from subprocess import Popen, PIPE


def function(input_data) -> str:
    password1 = input_data.split('\n')[0]
    password2 = input_data.split('\n')[1]

    if len(password1) < 8:
        result = 'Короткий!'
    elif password1 == password2:
        result = 'OK'
    else:
        result = 'Различаются.'
    return result


# input, result
test_variants = [
    "пароль\nпароль",
    "пароль123\nпароль123",
    "qwerty\nqwerty",
    "qwerty12312\nqwerty123",
    "1234\n1234",
    "1dddq\n1dddq",
    "1qweeqw\n1",
    "1131\n123113",
    "111qweweq1\n111qweweq1",
    "11123\n111231",
    "12323\nhgfhgf"
]


def testing(input_data: str) -> tuple:

    COMMAND = r"python ./instance/testing/lesson_3/task_13/test_file_13.py"
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
