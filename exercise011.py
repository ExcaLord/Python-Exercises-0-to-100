# Word count #

word = input("Which word you desire to count the letters")

for letters in word.split():
    print(len(letters))
