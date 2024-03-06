# [dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase alphabets (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.

ord_list = [v for v in range(ord('a'), ord('a') + 26)]
result_dict = {chr(ascii):ascii for ascii in ord_list}
print(result_dict)