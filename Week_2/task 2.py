sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0
for ch in sentence.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("Vowels =", vowels)
print("Consonants =", consonants)
