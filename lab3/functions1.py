def grams_to_ounces(grams):
    return grams * 28.3495231

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def permutations(s):
    if len(s) == 0:
        return ['']
    result = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            result.append(char + perm)
    return result

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * 3.141592653589793 * radius ** 3

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def is_palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
