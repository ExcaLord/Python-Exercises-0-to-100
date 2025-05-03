# Find the highest number #

list_of_numbers = [34, 45, 23, 657, 234, 2345, 2736, 7682]
highest_number = list_of_numbers[0]

for numbers in list_of_numbers:
    if numbers > highest_number:
        highest_number = numbers

print(f"The highest number is {highest_number}")
