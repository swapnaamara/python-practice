import copy

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

s1 = Student("Ravi", [90, 85])
s2 = copy.copy(s1) 
s3 = copy.deepcopy(s1) 

s1.marks[0] = 50
print(s2.marks) 
print(s3.marks) 
