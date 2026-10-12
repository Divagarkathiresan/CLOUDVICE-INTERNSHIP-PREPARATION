#check prime
import math

num=int(input("enter the number to check prime : "))    
if num < 2:
    print("It is not prime")

flag=True
for i in range(2,int(math.sqrt(num)) + 1):
        if(num%i==0):
            flag=False
            break
        
if flag==True:
    print("It is prime")
else:
    print("It is not prime")

