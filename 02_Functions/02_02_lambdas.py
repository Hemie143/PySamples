# Function
addition = lambda x, y: x + y
print(addition(2, 6))

# Equivalent
def addition(x, y):
    return x + y
print(addition(2, 6))

# Used in other functions
people = [('Anna', 20), ('Bob', 18), ('Charlie', 16), ('David', 19), ('Emily', 14)]
print(sorted(people, key=lambda x: x[1]))
