# Step 4: Handling a Win or Loss
# This demonstrates how to track game outcomes and display final results

import random

# Generate a random secret calibration value
secret_value = random.randint(1, 50)

# Print welcome message
print("Welcome to the Calibration Value Guessing Game!")
print("I'm thinking of a calibration value between 1 and 50.")
print("You have 5 tries to guess it!")

# Track whether the player has won
player_won = False

# Create the game loop with guessing logic
for attempt in range(5):
    print(f"\nAttempt {attempt + 1} of 5")
    
    # Get the player's guess
    guess = int(input("Enter your guess (1-50): "))
    
    # Check the guess
    if guess == secret_value:
        print("🎉 Congratulations! You've guessed correctly!")
        print(f"The secret value was {secret_value}!")
        player_won = True
        break  # Exit the loop early
    elif guess < secret_value:
        print("Too low! Try a higher value.")
    else:
        print("Too high! Try a lower value.")
    
    # Show remaining attempts
    remaining = 5 - (attempt + 1)
    if remaining > 0:
        print(f"You have {remaining} attempt(s) remaining.")

# Handle the final outcome
print("\n" + "=" * 50)
if player_won:
    print("🏆 You won! Well done!")
else:
    print("😔 Game Over! You've run out of attempts.")
    print(f"The secret value was {secret_value}.")

print("Thanks for playing the Calibration Value Guessing Game!")
print("=" * 50)
