# List comprehensions
# -> map
# -> filtering

# lambda

# Product data: (name, price, category, stock, sales)
products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  

product_names = []

for product in products:
  product_names.append(product[0])

print(product_names)

# Pythonic (idiomatic Python) -> likely to see in existing codebases

product_names = [ p[0] for p in products ]
print(product_names)

prices_with_tax = [ round(p[1] * 1.2, 2) for p in products ]
print(prices_with_tax)

def calculate_with_tax(price, tax_rate):
  """
  Pass in a decimal percentage to increase the price by, rounded to 2dp.
  """
  return round(price * (1 + tax_rate), 2)

# Version 1
prices_with_tax = [ calculate_with_tax(p[1], 0.2) for p in products ]

# Version 2
prices_with_tax = []

for product in products:
  prices_with_tax.append(calculate_with_tax(product[0], 0.2))

