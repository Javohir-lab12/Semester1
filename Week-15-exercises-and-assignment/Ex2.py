import random

counter = 1
number = random.randint(1,20)
while counter < 6:
    guess = input((f"Attempt {counter}/5. Enter your guess: "))
    guess = int(guess)
    if guess == number:
        print("You got it!")
        break
    if counter == 5:
        print("Game Over")
        print(f"The expected number is {number}")
        break
    if guess > number:
        counter += 1
        print("Too high!")
    if guess < number:
        counter += 1
        print("Too low!")