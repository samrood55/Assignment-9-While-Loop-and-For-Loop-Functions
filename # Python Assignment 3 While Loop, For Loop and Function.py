# Python Assignment 3: While Loop, For Loop and Function
# Complete solution based on the assignment PDF.

import random


# 1. WHILE LOOP & CONTROL STATEMENTS: NUMBER GUESSING GAME

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Out-of-range guesses do not consume an attempt.
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue

        attempts -= 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

        if attempts > 0:
            print("Attempts remaining:", attempts)
    else:
        # The while-else executes when attempts run out without a break.
        print("Better luck next time! The correct number was", secret_number)


# 2. FOR LOOP: MULTIPLICATION TABLE GENERATOR

def multiplication_table():
    try:
        number = int(input("Enter the number for which you want the multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


# 3. FUNCTION: BMI CALCULATOR

def calculate_bmi(weight, height):
    """Return BMI = weight in kilograms / (height in meters squared)."""
    return weight / (height ** 2)


def bmi_calculator():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers for weight and height.")


# MAIN PROGRAM: choose which assignment task to run

if __name__ == "__main__":
    print("PYTHON ASSIGNMENT 3")
    print("1. Number Guessing Game")
    print("2. Multiplication Table Generator")
    print("3. BMI Calculator")

    choice = input("Choose a program (1, 2, or 3): ").strip()

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        multiplication_table()
    elif choice == "3":
        bmi_calculator()
    else:
        print("Invalid choice. Please run the file again and choose 1, 2, or 3.")
