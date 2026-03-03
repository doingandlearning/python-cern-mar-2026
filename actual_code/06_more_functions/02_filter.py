products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  

electronic_products = []

for product in products:
  if product[2] == "Electronics":
    electronic_products.append((product[0], product[1]))

print(electronic_products)

electronic_products = [(p[0], p[1]) for p in products if p[2] == "Electronics"]
print(electronic_products)

inexpensive_products = [p for p in products if p[1] < 30]
print(inexpensive_products)

# map:  A -> B
# filter:  A -||-> A
# reduce: A -> 1


sale_values = []

for product in products:
  sale_values.append(product[1] * product[3])

net_income = sum(sale_values)
print(net_income)

net_income = sum([p[1] * p[3] for p in products])
print(net_income)