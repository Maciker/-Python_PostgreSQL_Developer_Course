"""def divide_secure(number, divisor):
    if divisor == 0:
        raise  ValueError("The divisor is 0")
    return number / divisor

print(divide_secure(10,0.5))

user_input = input('Enter a number: ')
if user_input == 0:
    # ask again"""

# the way of doind this with assertions
def divide_secure(number, divisor):
    assert divisor != 0, "Divided a number by 0"
    return number / divisor
# Improve the perfomance of the programm
