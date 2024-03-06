# [map] Write a Python function square_numbers that takes a list of integers as input and uses the map function to return a new list containing the square of each element.

def square_numbers(int_list):
    return list(map(lambda x:x**2, int_list))

nums = [1, 2, 3, 4, 5]
sqr_numbers = square_numbers(nums)
print(sqr_numbers)