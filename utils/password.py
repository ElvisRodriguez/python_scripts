import os
import string
import random


def generate_random_string(
    length, mixed_case=False, include_numbers=False, special_characters=False
):
    all_characters = [string.ascii_lowercase]
    if mixed_case:
        all_characters.append(string.ascii_uppercase)
    if include_numbers:
        all_characters.append(string.digits)
    if special_characters:
        all_characters.append(string.punctuation)
    all_characters = list(''.join(all_characters))
    random.shuffle(all_characters)
    all_characters = ''.join(all_characters)
    random_string = ''.join([random.SystemRandom().choice(all_characters) for _ in range(length)])
    return random_string