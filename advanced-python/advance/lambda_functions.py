"""l = lambda x: x > 5
print(l(10))

def alter(values, check):
    return [val for val in values if check(val)]

my_list = [1,2,3,4,5,6,7]
def check_not_five(x):
    return x!=5

another_list = alter(my_list, lambda x: x != 5)

list_without_lambda = alter(my_list, check_not_five)
print(list_without_lambda)
print(another_list)"""

def alter(values, check):
    # return list(filter(check, values)) the same result. En python we use list comprehension
    return [val for val in values if check(val)]

def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)

print(remove_numbers("hel5lo"))

print(skip_letter("hello", "o"))