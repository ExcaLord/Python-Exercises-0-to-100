# Reverse a String #

user_prhase = input("Type the prhase or word you want to reverse: ")

reversed_string = ""

for char in range(len(user_prhase) - 1, -1, -1):
    reversed_string += user_prhase[char]

print(reversed_string)
