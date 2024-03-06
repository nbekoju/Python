# [*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. Test your function with various input cases.
def calculate_sum(*args):
    sum = 0
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError("Input must be a number")
        sum += num 
    return sum 

sum = calculate_sum(12, 12.5, 14.9, 16)
print(sum)
sum = calculate_sum(12, 12.5, "abcd", 16)
print(sum)
