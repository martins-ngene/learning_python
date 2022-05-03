
# New line
print("Giraffe\nAcademy")

# Escape quotation marks
print("Giraffe \"Academy\"")

# String variables and concatenation

phrase = "Giraffe Academy"

print(phrase + "is cool")

# Using Functions to modify strings

# String to lowercase
print(phrase.lower())

# String to UPPERCASE
print(phrase.upper())

# Is string uppercase or lowercase
print(phrase.upper().isupper())
print(phrase.lower().islower())

# String length
print(len(phrase))

# Getting characters by index
print(phrase[0])

# Getting the index of characters
print(phrase.index("G"))

# Using the replace method
# With string
print(phrase.replace("Giraffe", "Zebra"))

# With variable
replace = "Elephant"
print(phrase.replace("Giraffe", replace))

# Other String Methods
# str.capitalize()
print(phrase.capitalize())

# str.casefold()
print(phrase.casefold())

