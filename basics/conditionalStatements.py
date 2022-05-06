# Syntax for conditional statements if, else statements

admin_login = False

if admin_login:
    print("Welcome, Mr Martins")
else:
    print("Access Denied")

# Chaining if else statements with elif

is_tall = False
is_muscular = False

if is_tall:
    print("You are tall")
elif is_muscular:
    print("You are muscular")
else:
    print("You're neither tall nor muscular")

# Using negation operator not() and or/not comparators


if is_muscular and is_tall:
    print("You are very fit for sports")
elif is_muscular and not is_tall:
    print("You need stretch exercise and you will be fine")
elif not is_muscular and is_tall:
    print("You need to hit the gym")
else:
    print("You need exercise")

# Comparison operators
# There are many comparison operators which we can use for checking conditions
# <, >, <=, >=, ==, !=


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2, 3, 4))

# Creating the above function with a math function


def max_num2(num1, num2, num3):
    return max(num1, num2, num3)


print(max_num2(2, 3, 4))
