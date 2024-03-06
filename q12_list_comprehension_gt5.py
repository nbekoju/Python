# [list comprehension] Given a list of strings, create a new list that contains only the strings with more than 5 characters using list comprehension.

strings_list = ["apple", "banana", "cat", "dog", "elephant", "fish"]
word_gt_5_char = [word for word in strings_list if len(word) > 5]
print(word_gt_5_char)