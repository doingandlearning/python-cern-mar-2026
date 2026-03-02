# STEP 5C: Split bill (ask how many people, must be >= 1, with friendly messages)

items = [
    {"id": 1, "name": "Coffee",   "price": 3.50},
    {"id": 2, "name": "Tea",      "price": 2.40},
    {"id": 3, "name": "Sandwich", "price": 5.95},
    {"id": 4, "name": "Cake",     "price": 3.25},
    {"id": 5, "name": "Fruit",    "price": 1.10},
]

total = 0.0
purchases = []

print("Welcome to the Fault-Tolerant Checkout")
print("Type 'done' at the item prompt to finish.\n")

while True:
    print("Menu:")
    for item in items:
        print(f"  {item['id']}. {item['name']} (£{item['price']:.2f})")

    choice = input("\nChoose a product number (1-5) or type 'done': ").strip().lower()
    if choice == "done":
        break

    try:
        choice_num = int(choice)
    except ValueError:
        print("You need to use valid numbers here (1-5). Try again.\n")
        continue

    if choice_num < 1 or choice_num > 5:
        print("We don't have that product. Please choose 1-5 from the menu.\n")
        continue

    chosen_item = None
    for item in items:
        if item["id"] == choice_num:
            chosen_item = item
            break

    if chosen_item is None:
        print("We don't have that product. Please choose 1-5 from the menu.\n")
        continue

    qty_text = input(f"How many {chosen_item['name']} would you like? ").strip()

    try:
        quantity = int(qty_text)
    except ValueError:
        print("Quantity must be a whole number (for example 1, 2, or 3). Try again.\n")
        continue

    if quantity < 1:
        print("Quantity must be at least 1. Try again.\n")
        continue

    if quantity > 20:
        print("That's too many for one order (max 20). Try again.\n")
        continue

    line_total = chosen_item["price"] * quantity
    total += line_total

    purchases.append({
        "name": chosen_item["name"],
        "unit_price": chosen_item["price"],
        "quantity": quantity,
        "line_total": line_total,
    })

    print(f"Added to basket: {chosen_item['name']} x{quantity} = £{line_total:.2f}")
    print(f"Running total: £{total:.2f}\n")

print("\nReceipt")
print("-" * 36)
for p in purchases:
    print(f"{p['name']} x{p['quantity']} @ £{p['unit_price']:.2f} = £{p['line_total']:.2f}")
print("-" * 36)
print(f"Total: £{total:.2f}")

while True:
    people_text = input("\nHow many people are splitting the bill? ").strip()

    try:
        people = int(people_text)
    except ValueError:
        print("You need to use a whole number here (for example 1, 2, or 3).")
        continue

    if people < 1:
        print("You need at least 1 person to split a bill. Try again.")
        continue

    break

per_person = total / people
print(f"\nSplit between {people}: each person pays £{per_person:.2f}")
