import re

def match_a_b(string):
    return bool(re.fullmatch(r'ab*', string))

def match_a_bb(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

def find_lowercase_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

def find_upper_lower(string):
    return re.findall(r'\b[A-Z][a-z]+\b', string)

def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

def snake_to_camel(string):
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

def insert_spaces_capital(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

def camel_to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()
