def isEven():
    return(num%2)

def getSmallest(num1, num2):
    small = num1
    if num1 > num2:
        small = num2
    return small

num = int(input("Enter your integer: \n"))
isEven()

if isEven():
    print("Odd")
else:
    print("Even")

num1 = int(input("Enter your first integer: \n"))
num2 = int(input("Enter your second number: \n"))

print("The smaller number is: ", getSmallest(num1,num2))

