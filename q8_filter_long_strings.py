# [filter] Write a Python function filter_long_strings that takes a list of strings as input and uses the filter function to return a new list containing strings with more than 5 characters.

def filter_long_strings(words):
    return list(filter(lambda x: len(x) > 5, words))

words = ["apple", "banana", "cat", "dog", "elephant"]
long_strings = filter_long_strings(words)
print(long_strings)