fruits = {'orange', 'apple', 'banana', 'pear', 'pear', 'banana'}
print('orange' in fruits) # check for membership!

colours = {'red', 'green', 'blue', 'orange'}

# 
home_country = ["France", "France", "Germany", "Norway", "Ireland", "France", "Switzerland", "Netherlands"]
unique_country = list(set(home_country))
unique_country.sort()
print(unique_country)

print(fruits.symmetric_difference(colours))