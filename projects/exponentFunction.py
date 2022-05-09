# A Custom Function which gives the cube root of a number

def to_power(num, power):
    result = 1
    for x in range(power):
        result = result * num
    return result


print(to_power(10, 4))

