from instance.testing import lesson_1, lesson_2, lesson_3


class Testing:

    def __init__(self, lesson, task):
        self.lesson = int(lesson)
        self.task = int(task)

    def test(self):
        if self.lesson == 1:
            if self.task == 1:
                return lesson_1.test_1.get_result()
            elif self.task == 2:
                return lesson_1.test_2.get_result()
            elif self.task == 3:
                return lesson_1.test_3.get_result()
            elif self.task == 4:
                return lesson_1.test_4.get_result()
            elif self.task == 5:
                return lesson_1.test_5.get_result()
        elif self.lesson == 2:
            if self.task == 1:
                return lesson_2.test_1.get_result()
            elif self.task == 2:
                return lesson_2.test_2.get_result()
            elif self.task == 3:
                return lesson_2.test_3.get_result()
            elif self.task == 4:
                return lesson_2.test_4.get_result()
            elif self.task == 5:
                return lesson_2.test_5.get_result()
        elif self.lesson == 3:
            if self.task == 1:
                return lesson_3.test_1.get_result()
            elif self.task == 2:
                return lesson_3.test_2.get_result()
            elif self.task == 3:
                return lesson_3.test_3.get_result()
            elif self.task == 4:
                return lesson_3.test_4.get_result()
            elif self.task == 5:
                return lesson_3.test_5.get_result()