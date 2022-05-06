# Creating a function

def say_hello():
    print("Hello World")


# Calling or invoking an existing function
say_hello()


# Passing arguments or function parameters
def say_intro(name, age):
    print("Hello World, my name is " + name + " and I am " + str(age) + " years old.")


# Calling a function that accepts parameters

say_intro("Martins", 1234)

# Return statements
# If we don't tell a function what to return, it returns nothing.


def cube(num):
    result = num * num * num
    return result


print(cube(2))
