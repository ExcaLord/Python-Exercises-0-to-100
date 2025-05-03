# Vocal count in a word #

word = str(input("Write the word you would like to know how many vocal have: "))

vowels = "aeiouAEIOU"

vowels_count = 0

for char in word:
    if char in vowels:
        vowels_count += 1
        
print(vowels_count)