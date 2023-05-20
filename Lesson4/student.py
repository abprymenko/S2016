from human import Human
class Student(Human):
    def __init__(self, name, age, height, group, subject, grade):
        super().__init__(name, age, height)
        self.Group = group
        self.Subject = subject
        self.Grade = grade
    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Group: {self.Group}\n" \
               f"Subject: {self.Subject}\n" \
               f"Grade: {self.Grade}"