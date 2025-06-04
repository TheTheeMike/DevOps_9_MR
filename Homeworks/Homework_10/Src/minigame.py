import random

def guess_number():
    R = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        num = int(input("Can you guess the number? : "))

        if num == R:
            print("Congratulations! You guessed the right number!")
            return
        elif num > R:
            print("Too high")
        else:
            print("Too low")

        attempts += 1

    print(f"Sorry, you've run out of attempts. The correct number was {R}")
    
guess_number()
