def findFactorial(num):
    if num==0 or num==1:
        return 1
    elif num==2:
        return 2

    return findFactorial(num-1)+findFactorial(num-2)

num=int(input("Enter the number : "))
print(f"The factorial of the number is {findFactorial(num)}")