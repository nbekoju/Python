# [set comprehension] Given a list of words, write a Python program to create a set using set comprehension that contains all the unique characters present in the words.


words = ["apple", "banana", "cat", "dog", "elephant"]

char_set = {char for word in words for char in word}

print(char_set)