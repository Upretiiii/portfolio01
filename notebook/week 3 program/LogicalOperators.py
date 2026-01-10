age = 30
print(age >= 18 and age <= 65)  # True
print(age < 18 or age > 65)     # False
print(not age > 18)             # False

# Combining logical operators with parentheses
print((age >= 18 and age <= 65) and (not age == 30))  # False

# Chaining relational operators
weight = 150
height = 150
print(100 < weight < 200)       # True
print(131 < height < 160)       # True
