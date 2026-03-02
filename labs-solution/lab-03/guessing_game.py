# Lab 3: Iteration and Control Flow - Complete Solution
# Guessing game: find the secret calibration value (1-50)

import random

# Step 1: Setting up the Game
print("=" * 50)
print("Welcome to the Calibration Value Guessing Game!")
print("=" * 50)
print("I'm thinking of a calibration value between 1 and 50.")
print("You have 5 attempts to guess it correctly!")
print()

# Generate the secret calibration value
secret_value = random.randint(1, 50)

# Step 2: Game Loop Setup
attempts = 5
player_won = False

# Step 3: The Main Game Loop
for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}")
    
    # Get the player's guess
    guess = int(input("Enter your guess (1-50): "))

    # Check if the guess is valid
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50!")
        continue

    # Check the guess
    if guess == secret_value:
        print("🎉 Congratulations! You've guessed correctly!")
        print(f"The secret value was {secret_value}!")
        player_won = True
        break
    elif guess < secret_value:
        print("Too low! Try a higher value.")
    else:
        print("Too high! Try a lower value.")
        
    # Show remaining attempts
    remaining = attempts - (attempt + 1)
    if remaining > 0:
        print(f"You have {remaining} attempt(s) remaining.")
    print()

# Step 4: Handle Win or Loss
print("=" * 50)
if player_won:
    print("🏆 You won! Well done!")
else:
    print("😔 Game Over! You've run out of attempts.")
    print(f"The secret value was {secret_value}.")

print("Thanks for playing the Calibration Value Guessing Game!")
print("=" * 50)
