"""
Generate a random string of variable types of characters.
"""
import string
import random


def generate_random_string(
    length, mixed_case=False, include_digits=False, special_characters=False
):
    """Generate a random string of characters.
    Args:
        - length(int): Desired length of string.
        - mixed_case(bool): Optional. Include lowercase and uppercase letters.
        - include_digits(bool): Optional. Include digits 0 - 9.
        - special_characters(bool): Optional. Include characters from: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    Returns:
        random_string(str): A random string of characters.
    """
    all_characters = [string.ascii_lowercase]
    if mixed_case:
        all_characters.append(string.ascii_uppercase)
    if include_digits:
        all_characters.append(string.digits)
    if special_characters:
        all_characters.append(string.punctuation)
    all_characters = list(''.join(all_characters))
    random.shuffle(all_characters)
    all_characters = ''.join(all_characters)
    random_string = ''.join([random.SystemRandom().choice(all_characters) for _ in range(length)])
    return random_string
