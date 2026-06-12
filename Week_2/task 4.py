import random
import string
characters = ""
length = int(input("Enter password length: "))
use_upper = input("Include uppercase? (yeso/no): ")
use_lower = input("Include lowercase? (yes/no): ")
use_digits = input("Include digits? (yes/no): ")
use_special = input("Include special characters? (yes/no): ")

characters = ""
if use_upper == "yes":
    characters += string.ascii_uppercase
if use_lower == "yes":
    characters += string.ascii_lowercase
if use_digits == "yes":
    characters += string.digit
if use_special == "yes":
     characters += string.punctuation
password = ""
for i in range(length):
    password += random.choice( characters)
print("generate Password:", password)
