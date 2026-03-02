# Step 1: Setting up the Game
# This demonstrates the basic setup for the guessing game

import random

# Generate a random secret calibration value
secret_value = random.randint(1, 50)

# Print welcome message
print("Welcome to the Calibration Value Guessing Game!")
print("I'm thinking of a calibration value between 1 and 50.")
print("You have 5 tries to guess it!")

# For debugging - remove this in the final game
print(f"Secret value: {secret_value}")
