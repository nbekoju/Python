# [list comprehension] Given three lists list1, list2, and list3, each containing integers, write a Python program using list comprehension to generate a new list of unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, such that x + y + z = 0.

list1 = [1 , 2, 3, 4]
list2 = [0, 2, 4, 1]
list3 = [-2, -1, -10, -5, -4]

result = [(x, y, z) for x in list1 for y in list2 for z in list3 if x + y + z == 0]

print(result)
