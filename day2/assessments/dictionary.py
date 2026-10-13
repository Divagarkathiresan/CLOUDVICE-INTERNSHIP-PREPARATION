students={}

marks=[81,90,45,78,82]

names=["Alex","Arjun","Divagar","Karthi","Rithish"]


for i in range(len(marks)):
    students[names[i]] = marks[i]

topper_student=""
topper_mark=0
for student in students:
    if(students[student] > topper_mark):
        topper_mark=students[student]
        topper_student=student

print(topper_student,topper_mark,sep=" ")