myList = [1,3,4,6,87]

for i in myList:
    print(i)

print("--------------------")

for i in range(0, len(myList)):
    print(myList[i])

print("--------------------")

i = 0
while i < len(myList) +1:
    print(myList[i])
    i += 1

print("------------------")

myList.append(200)
print(myList)

myList = myList + [1,2,4,12,3]
print(myList)

myList.insert(2,12)
print(myList)

print(myList[1:3])
print(myList[-3:])

print(max(myList))
print(min(myList))

print("--------------------")

colours = ['red','green','blue','purple','yellow','orange']
print(max(colours))
print(min(colours))

print('-----------------------')

myList.sort()
colours.sort()
print(myList)
print(colours)
