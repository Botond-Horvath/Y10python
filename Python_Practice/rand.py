import random

def sortKey(k):
    return k[1]

numbers = []
for i in range (1,100):
    numbers += [[random.randint(1,100),chr(random.randint(65,90))]]

numbers.sort()
numbers.sort(key=sortKey)
for n in numbers:
    print(n)