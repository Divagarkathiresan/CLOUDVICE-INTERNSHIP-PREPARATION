class Student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark

    def display(self):
        return f"{self.name} is {self.age} years old. He got {self.mark} marks"

name=input("Enter the name : ")
age=int(input("Enter the age : "))
mark=int(input("Enter the mark : "))


student1=Student(name,age,mark)
print(student1.display())
