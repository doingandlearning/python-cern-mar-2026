def add(a,b):
  return a + b

add(1,2)

def get_price_from_product(product):
  return product[1]

# lambda -> anonymous functions -> callable -> arrow functions
# small, throw-away functions

add = lambda a, b: a + b  # implicit return

add(1,2)

products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
] 



most_expensive = max(products, key=get_price_from_product)
most_expensive = max(products, key=lambda p: p[1])
print(most_expensive)

most_stock = max(products, key=lambda p: p[3]) 
print(most_stock)

print("=" * 22)
products.sort(key=lambda p: p[4])

for product in products:
  print(product)