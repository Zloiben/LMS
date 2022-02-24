import os


def get_result():
    """Ответ Hello, World!"""
    os.system('python .\\instance\\testing\lesson_1\\test_file_1.py >> '
              '.\\instance\\testing\lesson_1\\text_1.txt')
    with open(".\\instance\\testing\lesson_1\\text_1.txt", encoding="utf-8") as file:
        data = list(map(str.strip, file.readlines()))
        print(data[-1])
    return data[-1] == "Hello, World!"

