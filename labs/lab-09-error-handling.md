# Lab 9: The Fault-Tolerant Checkout

## Objective
Build a small checkout program that **never crashes** on invalid input. You'll use `try...except` to catch errors, validate ranges, and re-prompt the user until you get valid data. This is how robust programs handle real-world input.

You will:
1. Get a basic checkout working (menu, item choice, quantity, total)
2. Wrap risky conversions in `try...except` so bad input doesn’t crash the program
3. Validate ranges (e.g. menu 1–5, quantity ≥ 1)
4. Produce a receipt at the end
5. (Optional) Add one extra feature (discount code, undo, or split bill)

---

## Scenario: Fault-Tolerant Checkout

The program sells a few items at fixed prices. The user chooses an item by number and enters a quantity, then types `done` to finish and see a receipt. No matter what they type (letters, empty input, out-of-range numbers), the program should print a clear message and ask again instead of crashing.

---

## Task 1: Get It Working (No Error Handling Yet)

Create `lab_09_checkout.py` with a simple menu and loop.

**Your task:**

- Define a list of items with id, name, and price (e.g. Coffee £3.50, Tea £2.40, Sandwich £5.95, Cake £3.25, Fruit £1.10)
- In a loop, print the menu (numbered 1–5), ask for an item number, then ask for quantity
- Compute the line total and add it to a running total
- Let the user type `done` at the item prompt to exit the loop
- Print a total at the end

**Hints:**

- Use `input()` for item and quantity; convert to `int()` (it will crash on bad input — you’ll fix that in Task 2)
- If choice is `"done"`, `break` out of the loop

<details>
<summary>Starter code (optional)</summary>

```python
items = [
    {"id": 1, "name": "Coffee",   "price": 3.50},
    {"id": 2, "name": "Tea",      "price": 2.40},
    {"id": 3, "name": "Sandwich", "price": 5.95},
    {"id": 4, "name": "Cake",     "price": 3.25},
    {"id": 5, "name": "Fruit",    "price": 1.10},
]
total = 0.0
while True:
    print("Menu:")
    for item in items:
        print(f"  {item['id']}. {item['name']} (£{item['price']:.2f})")
    choice = input("\nChoose an item number (1-5) or type 'done': ").strip().lower()
    if choice == "done":
        break
    choice_num = int(choice)  # will crash on bad input
    # ... find chosen_item, ask quantity, add to total ...
```

</details>

---

## Task 2: Stop Crashes from Bad Numbers

Wrap the conversions to integer in `try...except` so the program never crashes on invalid input.

**Your task:**

- Where you call `int(choice)` and `int(qty_text)`, wrap each in a `try:` block
- Use `except ValueError:` to catch non-numeric input
- In the except block, print a helpful message and use `continue` to re-prompt

**Hints:**

- Keep the `try` block as small as possible (just the line that might raise)
- After handling the error, `continue` so the loop asks again

<details>
<summary>Possible pattern</summary>

```python
try:
    choice_num = int(choice)
except ValueError:
    print("Please enter a number 1-5 or 'done'.")
    continue
```

</details>

---

## Task 3: Validate Ranges

After parsing, check that values make sense.

**Your task:**

- Ensure menu choice is 1–5; if not, print a message and `continue`
- Ensure quantity is at least 1 (and optionally ≤ 20); if not, print a message and `continue`

**Hints:**

- Check `if choice_num < 1 or choice_num > 5:` and similar for quantity
- Handle “item not found” (e.g. no item with that id) and `continue`

<details>
<summary>Possible pattern for Task 3</summary>

```python
try:
    choice_num = int(choice)
except ValueError:
    print("Please enter a number 1-5 or 'done'.")
    continue
if choice_num < 1 or choice_num > 5:
    print("Please choose a number between 1 and 5.")
    continue
# ... find chosen_item ...
qty_text = input("Quantity? ").strip()
try:
    qty = int(qty_text)
except ValueError:
    print("Please enter a whole number.")
    continue
if qty < 1:
    print("Quantity must be at least 1.")
    continue
```

</details>

---

## Task 4: Produce a Receipt

Store each purchase (item name, unit price, quantity, line total) in a list and print a receipt at the end.

**Your task:**

- Create a list (e.g. `purchases`) and append a dict or tuple for each valid purchase
- When the user types `done`, loop over this list and print each line (e.g. "Coffee x2 = £7.00")
- Print the total at the end

**Hints:**

- Append after you’ve computed the line total
- Format with f-strings and e.g. `£{line_total:.2f}`

<details>
<summary>Possible pattern for Task 4</summary>

```python
purchases = []  # at start of script or loop
# After computing line_total for a valid choice and quantity:
purchases.append({"name": chosen_item["name"], "qty": qty, "line_total": line_total})
# When user types "done":
print("\nReceipt:")
for p in purchases:
    print(f"  {p['name']} x{p['qty']} = £{p['line_total']:.2f}")
print(f"Total: £{total:.2f}")
```

</details>

---

## Task 5: Add One “Real World” Feature (Optional)

Pick one: discount codes (e.g. SAVE10, FIVER), “undo” last item, or “split bill” (ask how many people, print per-person cost). Handle invalid input gracefully.

<details>
<summary>Possible approaches for Task 5</summary>

- **Discount code:** After printing the total, ask for a code; if it matches (e.g. `SAVE10`), multiply total by 0.9 and print the new total. Use `try`/`except` only if you ask for a number elsewhere.
- **Undo:** Keep the last purchase in a variable; if the user types `undo` at the item prompt (instead of a number or `done`), remove the last item from `purchases` and subtract its line total. Re-prompt.
- **Split bill:** After the receipt, ask "Split how many ways?"; use `try`/`except` for `int()` and check `>= 1`, then print `Total per person: £{total/n:.2f}`.

</details>

---

**You're done when** the checkout program runs with a menu, accepts items and quantities, and handles invalid input without crashing (and optionally includes one real-world feature).

---

## Key Concepts Demonstrated

- **`try...except`**: Catch specific exceptions (e.g. `ValueError`) so the program doesn’t crash
- **Validation**: Check ranges and meaning after parsing
- **`continue`**: Skip to the next loop iteration after an error
- **User feedback**: Clear messages so the user knows what went wrong

---

## Common Issues

- **Program still crashes on bad input** — Make sure every `int(...)` that uses user input is inside a `try` block with `except ValueError:` and that you `continue` (or re-prompt) so the loop doesn't use an invalid value.
- **Catching too much** — Use `except ValueError:` (or another specific exception) rather than `except Exception:` so you don't hide bugs like typos.
- **Wrong indentation** — The code that might raise (e.g. `int(choice)`) must be inside the `try` block; the message and `continue` must be inside the `except` block.
- **Menu choice 1–5** — After parsing the number, check the range and `continue` before you look up the item; otherwise an out-of-range number can cause an error when finding the chosen item.

---

## Next Steps

In the next lab, you’ll write automated tests for your analysis class (e.g. `ResultValue`) using pytest.
