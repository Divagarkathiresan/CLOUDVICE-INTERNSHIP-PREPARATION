list=[]
s="sdring"
list2=['d','i','v','a']
for c in s:
    list.append(c)


sets=set(list)
print(sets)

print(list[0:2])

list[0:2]='d','i'

print(list[0:2])

print(list)

list.extend(list2)
print(list)

tuple=tuple(list)

print(tuple)

print(list[5:3:-1])

# i=len(list)-1
# while(i>=0):
#     print(list[i])
#     i=i-1



def contains(fruit,c):
    flag=False
    for i in range(len(fruit)):
        if(fruit[i]==c):
            flag= True
            break
    return flag

fruits=["apple","orange","kiwi"]
ans=[]
for fruit in fruits:
    if(contains(fruit,'a')):
        ans.append(fruit)

copyList=fruits.copy()
print(copyList)

print(ans)


students={}
for i in range(1,4):
    students[i]=fruits[i-1]
print(students)

for rollno in students:
    print(students[rollno])