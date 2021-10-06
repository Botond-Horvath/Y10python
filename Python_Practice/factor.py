factorList = []

def factorCalc():
    n = 1
    while n < num +1:
        if  num % n == 0:
            factorList.append(n)
        n += 1

num = int(input("Please enter a whole number you want to factor: \n"))
factorCalc()

if len(factorList) == 2:
    print('0, ', str(factorList[1]), '(prime)')

else:
    print("Factors are: ") 
    print(*factorList, sep= ', ')
