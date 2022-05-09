# Writing a while loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("This is the end of the loop.")

# Writing for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating a string
for x in "fruits":
    print(x)

# Using the 'break' keyword
for x in "fruits":
    print(x)
    if x == "i":
        break

# Using the 'continue' keyword
letters = ["A", "B", "C", "D", "E"]
for x in letters:
    if x == "C":
        continue
    print(x)

# Using the range function
    utensils = ["plate", "spoon", "pot", "tray", "knife"]
    for item in range(len(utensils)):
        print(utensils[item])
