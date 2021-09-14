num1 = 122
num2 = 27

sum = num1+num2
product = num1*num2
division = num1/num2
integerDivision = num1//num2
modulus = sum%2

print("Sum: ", sum)
print("Product: ", product)
print("Division:", division)
print("Integer Division: ", integerDivision)

if modulus == 0:
    print("The sum is even")
else:
    print("The sum is odd")

grade = int(input("What grade did you recieve on your test? \n"))
if grade >= 90:
    print("A+")
elif grade >= 80:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")
