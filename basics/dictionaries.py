# Creating A Dictionary
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Accessing a dictionary
print(month_conversions["Dec"])

# Accessing a dictionary with the get() function to handle the "None" error
print(month_conversions.get("LA", "You entered an invalid key"))

# A Dictionary is an object with data type of 'dict'
print(type(month_conversions))

# Modifying a dictionary with the update() function which takes in only an iterable key/value pair or a dictionary
us_states = {
    "LA": "Los Angeles",
    "NO": "New Orleans",
}

us_states.update({"NJ": "New Jersey"})
print(us_states)

# Adding an item to a dictionary without the update() function
us_states["NY"] = "New York"
print(us_states)

# Removing items from dictionaries using del, pop(), clear(), and popitem()

# Removes the item with the specific key
us_states.pop("NY")
print(us_states)

# del, deletes the entire dictionary
ng_states = {
    "ABJ": "Abuja",
    "LAG": "Lagos",
}

del ng_states
# print(ng_states)

# clear() function, clears the entire dictionary
week_days = {
    "MON": "Monday",
    "TUE": "Tuesday",
}

week_days.clear()

print(week_days)

# popitem() function, removes the last inserted item on the dictionary
some_days = {
    "MON": "Monday",
    "TUE": "Tuesday",
}

print(some_days)
some_days["WED"] = "Wednesday"
