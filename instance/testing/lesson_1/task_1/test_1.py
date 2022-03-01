from subprocess import Popen, PIPE


def get_result():
    """Ответ Hello, World!"""
    result = "Hello, World!"
    command = r"python ./instance/testing/lesson_1/task_1/test_file_1.py"
    p = Popen(command, stdout=PIPE, stdin=PIPE, encoding='utf-8')
    out, err = p.communicate()
    return out.strip() == result


