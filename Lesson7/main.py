#1

#students = [1,2,3,4,5,6,7,8,9,"Andrii","Daniil"]
#range1 = iter(students)
'''
print(next(range1))#0
print(next(range1))#1
print(range1.__next__())#2
print(next(range1))#3
print(next(range1))#4
print(next(range1))#5
print(next(range1))#6
print(next(range1))#7
print(next(range1))#StopIteration
'''
'''
for i in range1:
    print(i)

while(True):
    try:
        print(range1.__next__())
    except StopIteration:
        break
'''
'''
from  counter import Counter
iter = Counter(20)
for i in iter:
    print(i)
while(True):
    try:
        print(iter.__next__())
    except StopIteration:
        break
'''
#2 - generator
'''
from generator import Generator
generator = Generator(7)
generator(6)
result = generator.Pow(10)
for i in result:
    print(i)
'''

#3 - closing
from decorator import Checker
checker = Checker()
#calculate = checker.Check(checker.Calculate)
#calculate("2/0")
while(True):
    digit1 = input("Enter digit1: ")
    digit2 = input("Enter digit2: ")
    operation = input("Enter operation: ")
    checker.Calculate(f"{digit1}{operation}{digit2}")