from instance.testing.lesson_1.task_1 import test_1
from instance.testing.lesson_1.task_2 import test_2


class Testing:

    def __init__(self, lesson, task):
        self.lesson = int(lesson)
        self.task = int(task)

    def test(self):
        if self.lesson == 1:
            if self.task == 1:
                return test_1.get_result()
            elif self.task == 2:
                return test_2.get_result()
