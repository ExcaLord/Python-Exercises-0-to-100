# Sum of numbers in a List #

numbers = []

while True:
    user_input = input("Digit each number that will be on the list: ").lower()

    if user_input == "done":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please insert a valid number or 'done' to finish")

total_sum = 0

for num in numbers:
    total_sum += num

print(total_sum)
