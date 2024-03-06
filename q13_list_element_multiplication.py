# [list comprehension] Given two lists of integers, create a list that contains the product of each element of the first list with the corresponding element in the second list using list comprehension.

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

result = [n1*n2 for n1, n2 in zip(num1, num2)]
print(result)
