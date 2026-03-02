items = [
    {"id": 1, "name": "Coffee",   "price": 3.50},
    {"id": 2, "name": "Tea",      "price": 2.40},
    {"id": 3, "name": "Sandwich", "price": 5.95},
    {"id": 4, "name": "Cake",     "price": 3.25},
    {"id": 5, "name": "Fruit",    "price": 1.10},
]

total = 0.0
purchases = []  # You will use this later for the receipt (Step 4)

print("Welcome to the Fault-Tolerant Checkout")
print("Type 'done' at any time at the item prompt to finish.\n")

while True:
    print("Menu:")
    for item in items:
        print(f"  {item['id']}. {item['name']} (£{item['price']:.2f})")

    choice = input("\nChoose an item number (1-5) or type 'done': ").strip().lower()
    if choice == "done":
        break

    # Step 1: This will crash on invalid input. You'll fix that in Step 2.
    choice_num = int(choice)

    # Find the chosen item
    chosen_item = None
    for item in items:
        if item["id"] == choice_num:
            chosen_item = item
            break

    if chosen_item is None:
        print("That item number doesn't exist.\n")
        continue

    qty_text = input(f"How many {chosen_item['name']}? ").strip()

    # Step 1: This will crash on invalid input. You'll fix that in Step 2.
    quantity = int(qty_text)

    line_total = chosen_item["price"] * quantity
    total += line_total

    # We'll build a proper receipt in Step 4
    print(f"Added: {chosen_item['name']} x{quantity} = £{line_total:.2f}")
    print(f"Running total: £{total:.2f}\n")

print("\nThanks! (Receipt comes in Step 4)")
print(f"Total: £{total:.2f}")