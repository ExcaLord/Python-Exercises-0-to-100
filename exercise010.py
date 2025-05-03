# Ordering a list #

list_of_numbers = []

while True:
    user_input = input(
        "Digit the numbers that will be organize for decimals use point: "
    )
    if user_input == "done" or user_input == "Done":
        break
    list_of_numbers.append(float(user_input))

n = len(list_of_numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if list_of_numbers[j] > list_of_numbers[j + 1]:
            list_of_numbers[j], list_of_numbers[j + 1] = (
                list_of_numbers[j + 1],
                list_of_numbers[j],
            )

print(list_of_numbers)
