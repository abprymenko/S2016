from Lesson4.student import Student
from Lesson4.sportsman import Sportsman
class Son(Student, Sportsman):
    def __init__(self, name, age, height, group, subject, grade, kindOfSports):
        super().__init__(name, age, height, group, subject, grade)
        self.KindOfSports = kindOfSports

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"{self.ShowInfo(self.KindOfSports)}"


        