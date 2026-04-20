import random
secret_number = random.randint(1, 100)
print("welcome to the number guessing game!")
print("I'm thinking between numbers 1 to 100!")
attempts=0
while True:
    num=int(input("guess the number between 1 to 100 :"))
    attempts+=1
    if num>secret_number:
        print("too high, try again!")
    elif num<secret_number:
        print("too low, try again!")
    else:
        print(f"congratulations, you got the number {secret_number} at your {attempts}th attempt!")
        break
