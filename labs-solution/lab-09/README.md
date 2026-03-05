# Lab 9: Fault-Tolerant Checkout — Solution

Reference solution for [Lab 9: The Fault-Tolerant Checkout](../labs/lab-09-error-handling.md).

## What’s in the solution

- **Task 1:** Menu (items 1–5 with id, name, price), loop, item choice, quantity, running total, `done` to finish.
- **Task 2:** `try`/`except ValueError` around `int(choice)` and `int(qty_text)` with a clear message and `continue`.
- **Task 3:** Range checks: menu choice 1–5, quantity ≥ 1 and (optionally) ≤ 20.
- **Task 4:** `purchases` list (name, qty, line_total); receipt at the end in the form `Coffee x2 = £7.00` and total.
- **Structure:** Logic in `main()` with `if __name__ == "__main__": main()` so the script only runs when executed directly.

Task 5 (optional real-world feature: discount code, undo, or split bill) is left for you to try.

## Run

```bash
python lab_09_checkout.py
```

Try invalid input (letters, empty, out-of-range numbers) to see the program re-prompt instead of crashing.
