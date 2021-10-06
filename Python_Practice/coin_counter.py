'''
This program includes 3 parts that are made up of 3 separate problems that we were given in class
'''

amount = int(input("Please enter the amount of money in cents: \n"))
toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5

remainder = amount % 5
if remainder < 3:
    amount -= remainder
else: 
    amount += (5-remainder)

toonieNum = amount // toonie
amount %= toonie
loonieNum = amount // loonie
amount %= loonie
quarterNum = amount // quarter
amount %= quarter
dimeNum = amount // dime
amount %= dime
nickelNum = amount // nickel
amount %= nickel

report = (str(toonieNum) + " toonies, \n" + str(loonieNum) + " loonies, \n" + str(quarterNum) + " quarters, \n" + str(dimeNum) + " dimes, \n" + str(nickelNum) + " nickles, \n")
print(report)