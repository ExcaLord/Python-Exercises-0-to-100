# Count vowels in a string #

user_phrase = input("Which phrase or word you want to count the vowels: ")
vowels = "aeiouAEIOU"
vowel_quantity = 0

for char in user_phrase:
    if char in vowels:
        vowel_quantity += 1

print(vowel_quantity)
