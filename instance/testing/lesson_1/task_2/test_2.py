import os


def test_1():
    os.system('python .\\instance\\testing\lesson_1\\task_2\\test_file_2.py >> '
              '.\\instance\\testing\lesson_1\\task_2\\text_2.txt')
    # os.system('1')
    # os.system('2')
    # os.system('3')
    with open(".\\instance\\testing\lesson_1\\task_2\\text_2.txt", encoding="utf-8") as file:
        data = list(map(str.strip, file.readlines()))
        print(data)


def test_2():
    pass


def get_result():
    """Ответ Hello, World!"""
    os.system('python .\\instance\\testing\lesson_1\\task_1\\test_file_1.py >> '
              '.\\instance\\testing\lesson_1\\task_1\\text_1.txt')
    with open(".\\instance\\testing\lesson_1\\task_1\\text_1.txt", encoding="utf-8") as file:
        data = list(map(str.strip, file.readlines()))
        print(data[-1])
    return data[-1] == "Hello, World!"
