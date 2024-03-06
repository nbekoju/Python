# [reduce] Implement a function called concatenate_strings that takes a list of strings as input and uses the reduce function to return a single string containing the concatenation of all the elements.

from functools import reduce

def concatenate_strings(words):
    return reduce(lambda x, y: x + " " + y, words)

words = ["apple", "banana", "cat", "dog", "elephant"]
concat_string = concatenate_strings(words)
print(concat_string)