num = 1.0
while (num <= 10):
    print(num)
    num = num + .1
    num = round(num, 1)

#
import random
secretNumber = random.randint(50, 100)
guess = None
print("welcome to the number guessing game.")
print("I have selected a number between 50 and 100. Try to guess it.")

while guess!= secretNumber:
    guess = int(input("Enter your guess: "))
    if guess < secretNumber:
        print("Too low. Try again.")
    elif guess > secretNumber:
        print("Too high. Try again.")
else:
    print(f"Congratulations! You guessed the correct number.")

