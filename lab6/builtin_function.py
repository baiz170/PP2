import math
import time
import functools

def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return {'upper': upper_count, 'lower': lower_count}

def is_palindrome(s):
    return s == s[::-1]

def sqrt_after_delay(num, delay_ms):
    time.sleep(delay_ms / 1000.0)
    return f'Square root of {num} after {delay_ms} miliseconds is {math.sqrt(num)}'

def all_true(t):
    return all(t)

print(multiply_list([1, 2, 3, 4]))
print(count_case('Hello World!'))
print(is_palindrome('racecar'))
print(sqrt_after_delay(25100, 2123))
print(all_true((True, True, False)))
