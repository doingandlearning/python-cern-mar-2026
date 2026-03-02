# Step 2: The Game Loop
# This demonstrates the loop structure for the guessing game

import random

# Generate a random secret calibration value
secret_value = random.randint(1, 50)

# Print welcome message
print("Welcome to the Calibration Value Guessing Game!")
print("I'm thinking of a calibration value between 1 and 50.")
print("You have 5 tries to guess it!")

# Create the game loop
for attempt in range(5):
    print(f"\nAttempt {attempt + 1} of 5")
    print("This is where the guessing logic will go!")
    
    # For now, just show the loop is working
    print(f"Loop iteration {attempt + 1}")


print("\nLoop finished!")

# For debugging - remove this in the final game
print(f"Secret value was: {secret_value}")
