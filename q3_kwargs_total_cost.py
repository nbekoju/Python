# [**kwargs] Write a Python function calculate_total_cost that calculates the total cost of items purchased from a store. The function should accept multiple keyword arguments, where the key is the item name, and the value is the item's price. The function should return the total cost of all items.

def calculate_total_cost(**kwargs):
    total_cost = 0
    for key, value in kwargs.items():
        total_cost += value 
    return total_cost

total_cost = calculate_total_cost(keyboard = 500, mouse = 300, monitor = 2000, cpu = 30000)
print(total_cost)