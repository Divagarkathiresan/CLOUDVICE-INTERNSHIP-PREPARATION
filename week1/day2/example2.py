# functions

# def printOutput(name, com="cloudvice"):
#     print(name,com,sep=" ")

# printOutput("dva")



def printNumbers(num):

    print(num)

    if(num==1):
        return num
    
    printNumbers(num-1)

printNumbers(5)




val=[1,2,3]

for i in range(len(val)):
    val[i] = lambda a : a + 10



import json

j={
    "name":"Divagar",
    "age":20
}
print(j)
print(type(j))


ja=json.dumps(j)


print(ja)
print(type(ja))


