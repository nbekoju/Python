# [reduce] Write a Python function calculate_factorial that takes an integer as input and uses the reduce function to return the factorial of that number.

from functools import reduce

def calculate_factorial(num: int):
    num_list = range(1, num + 1)
    return reduce(lambda x, y: x*y, num_list)

num = 6
factorial = calculate_factorial(num)
print(factorial)