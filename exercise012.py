# Multiply Table

number = int(input("Which multiply table you desire to know see: "))

for num in range(1, 11):
    table = num * number
    print(f"The result of {number} * {num} is equal to = {table}")
