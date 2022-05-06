# Working with list functions

colleagues = ["Collins", "Abigail", "Melisa", "Kelvin"]
numbers = [23, 34, 9, 7, 123]

print(colleagues, numbers)

# Add two lists together using the extend() function
colleagues.extend(numbers)
print(colleagues)

# Adding a new item to the end of a list using the append() function
colleagues.append("Kelly")
print(colleagues)

# Adding a new item to the front of another item in the list using the insert() function
colleagues.insert(0, "Joshua")
print(colleagues)

# Remove an item from a list using the remove() function
colleagues.remove(123)
print(colleagues)

# To empty a list using the clear() function
people = ["Collins", "Abigail", "Melisa", "Kelvin"]
people.clear()
print(people)

# Remove an element from the end of a list using the pop() function
category = ["tech", "agro", "medicine", "edu"]
category.pop()
print(category)

# Check for the index of a list item using the index() function
print(category.index("agro"))
# It returns an error if the item is not in the list

# Count how many times an item is present in a list using the count() function
numerical = [1,1,1,2,3,4,5,6,7,70]
print(numerical.count(1))

# Sort a list alphabetically and numerically in ascending order using the sort() function
alphabets = ["B", "D", "C", "A", "Z", "Y", "X"]
numerics = [0,9,8,7,6,5,4,3,2,1]
alphabets.sort()
numerics.sort()
print(alphabets, numerics)

# Reverse it to descending order using sort(reverse=True)
alphas = ["B", "D", "C", "A", "Z", "Y", "X"]
nums = [0,9,8,7,6,5,4,3,2,1]
alphas.sort(reverse=True)
nums.sort(reverse=True)
print(alphas, nums)

# Reverse a list using the reverse() function
alpha = ["D", "C", "B", "A"]
alpha.reverse()
print(alpha)

# Copy a list using the copy() function
copy_alpha = alpha.copy()
print(copy_alpha)
