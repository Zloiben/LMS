from instance.testing.lesson_1.task_1 import test_1
from instance.testing.lesson_1.task_2 import test_2
from instance.testing.lesson_1.task_3 import test_3
from instance.testing.lesson_1.task_4 import test_4
from instance.testing.lesson_1.task_5 import test_5

from instance.testing.lesson_2.task_6 import test_6
from instance.testing.lesson_2.task_7 import test_7
from instance.testing.lesson_2.task_8 import test_8
from instance.testing.lesson_2.task_9 import test_9
from instance.testing.lesson_2.task_10 import test_10

from instance.testing.lesson_3.task_11 import test_11
from instance.testing.lesson_3.task_12 import test_12
from instance.testing.lesson_3.task_13 import test_13
from instance.testing.lesson_3.task_14 import test_14
from instance.testing.lesson_3.task_15 import test_15

from instance.testing.lesson_4.task_16 import test_16
from instance.testing.lesson_4.task_17 import test_17
from instance.testing.lesson_4.task_18 import test_18
from instance.testing.lesson_4.task_19 import test_19
from instance.testing.lesson_4.task_20 import test_20


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
            elif self.task == 3:
                return test_3.get_result()
            elif self.task == 4:
                return test_4.get_result()
            elif self.task == 5:
                return test_5.get_result()
        elif self.lesson == 2:
            if self.task == 6:
                return test_6.get_result()
            elif self.task == 7:
                return test_7.get_result()
            elif self.task == 8:
                return test_8.get_result()
            elif self.task == 9:
                return test_9.get_result()
            elif self.task == 10:
                return test_10.get_result()
        elif self.lesson == 3:
            if self.task == 11:
                return test_11.get_result()
            elif self.task == 12:
                return test_12.get_result()
            elif self.task == 13:
                return test_13.get_result()
            elif self.task == 14:
                return test_14.get_result()
            elif self.task == 15:
                return test_15.get_result()
        elif self.lesson == 4:
            if self.task == 16:
                return test_16.get_result()
            elif self.task == 17:
                return test_17.get_result()
            elif self.task == 18:
                return test_18.get_result()
            elif self.task == 19:
                return test_19.get_result()
            elif self.task == 20:
                return test_20.get_result()