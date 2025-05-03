# Even or Odd

number1 = int(
    input("Introduce an integer number and we will say if is Even or Odd")
)

if number1 % 2 == 0:
    print("Is Even!")
elif number1 % 2 == 1:
    print("Is Odd!")
else:
    print("Incorrect input")