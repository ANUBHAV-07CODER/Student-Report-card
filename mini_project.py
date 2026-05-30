#STUDENT REPORT CARD SYSTEM
n = int(input("enter no. of student:"))
class student:
    def __init__(self,name,math,science,english,hindi,python):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
        self.hindi = hindi
        self.python=python
    def introduce(self):
        print(f"Name : {self.name}")
    def sub_marks(self):
        print(f"math : {self.math}")
        print(f"science : {self.science}")
        print(f"english : {self.english}")
        print(f"hindi : {self.hindi}")
        print(f"python : {self.python}")
    def total(self):
        total = self.math + self.python + self.hindi + self.english + self.science
        return total
    def avg(self):
        return self.total()/5
    def grade(self):
        avg = self.avg()
        if avg>=90:
            return "A+"
        elif avg >=80:
            return "A"
        elif avg>=70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "D"
    def report(self):
         print("="*30)
         self.introduce()
         self.sub_marks()
         print(f"total : {self.total()}")
         print(f"average: {self.avg():.2f}%")
         print(f"grade: {self.grade()}")
         print("="*30)

students = []
for i in range(n):
    print(f"\nenter detail of student{i+1}")
    name= input("name:")
    math = int(input("math:"))
    science = int(input("science:"))
    english = int(input("english:"))
    hindi = int(input("hindi:"))
    python = int(input("python:"))
    s = student(name,math,science,english,hindi,python)
    students.append(s)
print("report card")
for s in students:
    s.report()
