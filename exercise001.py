# Create a program that asks the user their name and age,
# then print a message that welcome the user
# and tell how old they will be in 5 years.

name = input("What is your name?")
age = int(input("What is your age?"))

print(
    f"Hello {name}, welcome to this exercise, awesome so you have {
        age
    } years old, and that in 5 years you will be {age + 5} years old."
)
