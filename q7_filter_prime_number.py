# [filter] Implement a function called filter_prime_numbers that takes a list of integers as input and uses the filter function to return a new list containing only the prime numbers.

def is_prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False 
    return True

def filter_prime_numbers(integer_list):
    return list(filter(lambda x: is_prime(x), integer_list))

nums = [1, 2, 3, 4, 5, 7, 9, 13, 16]
prime_nums = filter_prime_numbers(nums)
print(prime_nums)
