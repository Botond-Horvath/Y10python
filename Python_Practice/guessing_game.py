import random
num = random.randint(1,100)

print("This is a simple guessing game program. A random number was generalted between \n1 and 100. You have 7 guesses to guess this number. Good luck!\n")

n = 1
while n < 8 and guess != num:
    guess = int(input("Guess " + str(n) + ":\n"))
    if guess > num:
        print("lower!")
    elif guess < num:
        print("higher!")
    n += 1

print("The number was " + str(num))