# Given an array of strings (str), group the anagrams together. You can return the answer in any order.

from collections import defaultdict

def get_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for first_word in string_list:
        for second_word in string_list:
            if sorted(first_word) == sorted(second_word):
                anagram_groups[first_word].append(second_word)

    return anagram_groups

word_list = ["silent", "listen", "enlist", "apple", "elppa", "banana", "cat", "act"]

anagram_group = get_anagrams(word_list)
print(anagram_group)
