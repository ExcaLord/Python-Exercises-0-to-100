# Highest number from user input #

list_of_numbers = []

while True:
    number_input = input(
        "Insert the numbers you want to find the highest one and done to finish the "
        "input of numbers: "
    )

    if number_input == "done" or number_input == "Done":
        break
    list_of_numbers.append(float(number_input))

highest_number = list_of_numbers[0]

for numbers in list_of_numbers:
    if numbers > highest_number:
        highest_number = numbers

print(f"The highest number is {highest_number}")
