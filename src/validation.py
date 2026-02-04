from typing import Callable, List


def has_min_length(password: str, length: int = 8) -> bool:
    count = 0
    for _ in password:
        count += 1
    return count >= length


def has_digit(password: str) -> bool:
    for char in password:
        if '0' <= char <= '9':
            return True
    return False


def has_uppercase(password: str) -> bool:
    for char in password:
        if 'A' <= char <= 'Z':
            return True
    return False


def has_lowercase(password: str) -> bool:
    for char in password:
        if 'a' <= char <= 'z':
            return True
    return False


def has_special_character(password: str) -> bool:
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    for char in password:
        for special in special_characters:
            if char == special:
                return True
    return False


def has_no_spaces(password: str) -> bool:
    for char in password:
        if char == " ":
            return False
    return True


def is_valid(password: str) -> bool:
    if password == "":
        return False

    rules: List[Callable[[str], bool]] = [
        has_min_length,
        has_digit,
        has_uppercase,
        has_lowercase,
        has_special_character,
        has_no_spaces,
    ]

    for rule in rules:
        if rule(password) is False:
            return False

    return True
