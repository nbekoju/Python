# [set comprehension] Given two strings, write a Python program to create a set using set comprehension that contains all the characters that are common in both strings.


first_word = "apple"
second_word = "elephant"

common_char = {char for char in first_word if char in second_word}
print(common_char)