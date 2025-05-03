# Random number in a context generation
import random

first_range = int(input("Insert the first number: "))
second_range = int(input("Insert the limit of the randomize: "))
random_number = random.randint(first_range, second_range)

print(
    f"You random number is: {random_number}, that is between {first_range} and {
        second_range
    }"
)
