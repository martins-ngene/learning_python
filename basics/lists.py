# Working with lists (arrays)

# Declare a simple list and access the items of the list by positive index
friends = ["Kora", "Kent", "Kim"]
print(friends[0])

# Declare a simple list and access the items of the list by negative index
friends = ["Kelvin", "Karen", "Jim"]
print(friends[-1])

# Access a specific list item and every other item following it
others = ["Kelvin", "Karen", "Jim", "Kai"]
print(others[1:])

# Access a specific range of list items
others = ["Kelvin", "Karen", "Jim", "Kai", "Mora", "Roy"]
# Prints out items with index 1,2 but doesn't include the third
print(others[1:3])


# Access the item of a list which is the item of another list
listOfLists = [["Kora", "Kent", "Kim"], ["Kelvin", "Karen", "Jim"], ["Kelvin", "Karen", "Jim", "Kai"]]
print(listOfLists[0][0])

# Modify a list item
names = ["Kelvin", "Karen", "Jim", "Kai", "Mora", "Roy"]
names[2] = "Martins"
print(names)
