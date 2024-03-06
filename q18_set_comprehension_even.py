# [set comprehension] Given a list of numbers, create a set using set comprehension that contains only unique even numbers.

nums = [2, 4, 5, 6, 2, 5, 6, 3, 9]
even_set = {num for num in nums if num % 2 == 0}
print(even_set)