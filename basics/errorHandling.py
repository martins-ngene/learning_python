
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError as error:
    print(error)
