# Lab 3: Building a Calibration Value Guessing Game with Control Flow

## Objective
In this lab, you'll build an interactive guessing game where the computer picks a secret "calibration value" (a number between 1 and 50) and the player tries to guess it. You'll use `for` or `while` loops, `if/elif/else`, and `break` - similar to how interactive tools respond to user input.

You will:
1. Use loops to give the player multiple attempts
2. Use `if/elif/else` for conditional logic
3. Use `break` to exit a loop when the guess is correct
4. Track whether the player won or lost and display the result

---

## Scenario: Calibration Value Guessing Game

The program randomly selects a secret value between 1 and 50 (like a sensor reading range). The player has a fixed number of attempts to guess it. After each guess, the program says whether the guess was too high, too low, or correct. The game ends when the player guesses correctly or runs out of attempts.

---

## Task 1: Set Up the Game Structure

Create a file `guessing_game.py`:

**Your task:**

- Import the `random` module
- Create a variable to store the secret calibration value using `random.randint(1, 50)`
- Print a welcome message that explains the rules (range 1–50, number of attempts)
- Decide how many attempts the player gets (e.g. 5)

**Hints:**

- Use `import random` at the top of the file
- `random.randint(a, b)` returns a random integer N such that `a <= N <= b`
- Make the welcome message clear and friendly

<details>
<summary>Possible Solution for Task 1</summary>

```python
import random

secret_value = random.randint(1, 50)
attempts = 5

print("=" * 50)
print("Welcome to the Calibration Value Guessing Game!")
print("=" * 50)
print("I'm thinking of a calibration value between 1 and 50.")
print(f"You have {attempts} attempts to guess it!")
print()
```

</details>

---

## Task 2: Create the Game Loop

Add a loop that runs once per attempt.

**Your task:**

- Use a loop that runs exactly the number of attempts (e.g. `for attempt in range(attempts):`)
- Inside the loop, print which attempt this is (e.g. "Attempt 1 of 5")
- Leave space for the guessing logic in the next task

**Hints:**

- A `for` loop with `range(attempts)` runs the right number of times
- `range(5)` produces 0, 1, 2, 3, 4 — use `attempt + 1` when displaying to the user

<details>
<summary>Possible Solution for Task 2</summary>

```python
player_won = False

for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}")
    # Guessing logic will go here
```

</details>

---

## Task 3: Get the Guess and Give Feedback

Inside the loop, get the player's guess and compare it to the secret value.

**Your task:**

- Ask for the player's guess with `input()` and convert it to an integer
- If the guess is less than 1 or greater than 50, print a message and use `continue` to skip to the next attempt (optional)
- Use `if/elif/else` to check:
  - If `guess == secret_value`: print a success message, set a variable so you know they won, and use `break` to exit the loop
  - Elif `guess < secret_value`: print "Too low! Try a higher value."
  - Else: print "Too high! Try a lower value."
- Optionally print how many attempts remain

**Hints:**

- `input()` returns a string; use `int(...)` to convert
- Use `break` to exit the loop as soon as they guess correctly
- Use a variable (e.g. `player_won = True`) so that after the loop you can tell if they won

<details>
<summary>Possible Solution for Task 3</summary>

```python
for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}")
    guess = int(input("Enter your guess (1-50): "))

    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50!")
        continue

    if guess == secret_value:
        print("Congratulations! You've guessed correctly!")
        print(f"The secret value was {secret_value}!")
        player_won = True
        break
    elif guess < secret_value:
        print("Too low! Try a higher value.")
    else:
        print("Too high! Try a lower value.")

    remaining = attempts - (attempt + 1)
    if remaining > 0:
        print(f"You have {remaining} attempt(s) remaining.")
    print()
```

</details>

---

## Task 4: Display the Final Result

After the loop ends, show whether the player won or lost.

**Your task:**

- If the player won (you tracked this with a variable), print a congratulatory message
- If the player lost, print a message and show the secret value
- Print a closing message (e.g. "Thanks for playing!")

**Hints:**

- Use `if player_won:` ... `else:` after the loop
- The variable `guess` still holds their last guess; `secret_value` is unchanged

<details>
<summary>Possible Solution for Task 4</summary>

```python
print("=" * 50)
if player_won:
    print("You won! Well done!")
else:
    print("Game Over! You've run out of attempts.")
    print(f"The secret value was {secret_value}.")

print("Thanks for playing the Calibration Value Guessing Game!")
print("=" * 50)
```

</details>

---

## Extensions (if you finish early)

Try one or both of these once the main game works.

### Extension A: Use a `while` loop instead

**Your task:**

- Replace the `for attempt in range(attempts):` loop with a `while` loop
- Use a variable (e.g. `attempt = 0`) and increment it each time (e.g. `attempt += 1`)
- The loop should run while `attempt < attempts` (and optionally while the player hasn’t won yet)
- Make sure you don’t create an infinite loop: the attempt counter must increase and the loop must end when attempts are used up or the player guesses correctly

**Hints:**

- Initialise `attempt = 0` before the loop
- At the end of each iteration (after processing the guess), add `attempt += 1`
- You can use `while attempt < attempts and not player_won:` or break out with `break` when they win

<details>
<summary>Possible approach for Extension A</summary>

```python
attempt = 0
player_won = False

while attempt < attempts:
    print(f"Attempt {attempt + 1} of {attempts}")
    guess = int(input("Enter your guess (1-50): "))
    # ... same validation and comparison logic ...
    attempt += 1  # only increment for a "real" attempt (see Extension B)
```

</details>

---

### Extension B: Add a cheat code

**Your task:**

- If the player enters a special value (e.g. `-1`) as their guess, reveal the secret value and **do not** count it as an attempt
- Use `continue` to skip the rest of the loop so you don’t increment the attempt counter or check win/lose
- Only increment the attempt counter (in a `while` version) or only “use up” an attempt (in a `for` version) when the guess is not the cheat code

**Hints:**

- Check for the cheat value (e.g. `if guess == -1:`) **before** you check if they won or increment attempts
- Print something like "The secret value is 42" then `continue`
- In a `for` loop, the cheat doesn’t increment the loop variable, so that attempt is effectively free

<details>
<summary>Possible approach for Extension B</summary>

```python
guess = int(input("Enter your guess (1-50): "))

# Cheat code: -1 reveals the answer and doesn't count as an attempt
if guess == -1:
    print(f"(Cheat) The secret value is {secret_value}")
    continue

# Rest of your logic: range check, then correct / too low / too high
```

</details>

---

## Example Interaction

```
==================================================
Welcome to the Calibration Value Guessing Game!
==================================================
I'm thinking of a calibration value between 1 and 50.
You have 5 attempts to guess it!

Attempt 1 of 5
Enter your guess (1-50): 25
Too low! Try a higher value.
You have 4 attempt(s) remaining.

Attempt 2 of 5
Enter your guess (1-50): 40
Too high! Try a lower value.
You have 3 attempt(s) remaining.

Attempt 3 of 5
Enter your guess (1-50): 32
Congratulations! You've guessed correctly!
The secret value was 32!

==================================================
You won! Well done!
Thanks for playing the Calibration Value Guessing Game!
==================================================
```

---

## Key Concepts Demonstrated

- **Loops**: `for attempt in range(n)` for a fixed number of attempts
- **Conditional logic**: `if/elif/else` to compare guess and secret value
- **`break`**: Exit the loop early when the guess is correct
- **`continue`** (optional): Skip invalid input and go to the next iteration
- **Boolean flag**: A variable like `player_won` to record the outcome
- **Random numbers**: `random.randint(a, b)` for the secret value

---

## Common Issues

- **NameError: name 'random' is not defined** — Add `import random` at the top.
- **ValueError: invalid literal for int()** — The user entered non-numeric input; we don’t handle that yet.
- **Game doesn’t end when correct** — Use `break` when `guess == secret_value`.

---

## Next Steps

In the next lab, you’ll work with lists and use them to analyse collections of data (e.g. experimental readings).
