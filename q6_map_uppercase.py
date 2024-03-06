# [map] Create a function convert_to_uppercase that takes a list of strings as input and uses the map function to return a new list with all the strings converted to uppercase.

def convert_to_uppercase(words):
    return list(map(lambda x:x.upper(), words))

words = ["apple", "banana", "cat"]
upper_case_words = convert_to_uppercase(words)
print(upper_case_words)