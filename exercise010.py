# Ordering a list #

list_of_numbers = []

while True:
    user_input = input(
        "Digit the numbers that will be organize for decimals use point instead of comma: "
    )
    if user_input == "done" or user_input == "Done":
        break
    list_of_numbers.append(float(user_input))

print(sorted(list_of_numbers))
