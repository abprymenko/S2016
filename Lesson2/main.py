from student import Student
anton = Student("Anton", 14, "S2016")
andrii = Student("Andrii", 12, "S2016")
radomyr = Student("Radomyr", 11, "S2016")
kyrylo = Student("Kyrylo", 12, "S2016")
ivan = Student("Ivan", 12, "S2016")

students = list()
students.append(anton)
students.append(andrii)
students.append(radomyr)
students.append(kyrylo)
students.append(ivan)

for student in students:
    student.ToString()