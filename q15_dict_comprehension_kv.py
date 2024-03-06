# [dictionary comprehension] Given two lists one containing keys and another containing values, create a dictionary using dictionary comprehension.

keys = ["keyboard", "mouse", "monitor", "headphone"]
values = [500, 300, 2000, 30000]

price = {key:value for key, value in zip(keys, values)}
print(price)