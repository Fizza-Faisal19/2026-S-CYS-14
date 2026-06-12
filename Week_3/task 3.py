upper = lambda text: text.upper()
def invert(word):
    print(word[::-1])
text = input("Enter a string: ")
result = upper(text)
print("Uppercase:", result)
invert(result)
