import copy

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks # list

s1 = Student("Ravi", [90, 85])
s2 = copy.copy(s1) # shallow copy
s3 = copy.deepcopy(s1) # deep copy

s1.marks[0] = 50
print(s2.marks) # [50, 85] -> changed because shallow
print(s3.marks) # [90, 85] -> unchanged because deep