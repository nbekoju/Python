# [*args] Write a Python function concat_strings that takes any number of strings as arguments and returns a single concatenated string.

def concat_strings(*args):
    return " ".join(args)

result = concat_strings("apple", "banana", "cat")
print(result)