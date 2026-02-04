import pytest
from src.validator import (
    is_valid,
    has_min_length,
    has_digit,
    has_uppercase,
    has_lowercase,
    has_special_character,
    has_no_spaces,
)

# -------------------------
# Core validation tests
# -------------------------

def test_empty_password_is_invalid():
    assert is_valid("") is False


def test_valid_password():
    assert is_valid("Strong@123") is True


# -------------------------
# Minimum length rule
# -------------------------

def test_password_shorter_than_min_length_is_invalid():
    assert has_min_length("Ab@12") is False


def test_password_meets_min_length_is_valid():
    assert has_min_length("Abcd@123") is True


# -------------------------
# Digit rule
# -------------------------

def test_password_without_digit_is_invalid():
    assert has_digit("Password@") is False


def test_password_with_digit_is_valid():
    assert has_digit("Password1@") is True


# -------------------------
# Uppercase rule
# -------------------------

def test_password_without_uppercase_is_invalid():
    assert has_uppercase("password@1") is False


def test_password_with_uppercase_is_valid():
    assert has_uppercase("Password@1") is True


# -------------------------
# Lowercase rule
# -------------------------

def test_password_without_lowercase_is_invalid():
    assert has_lowercase("PASSWORD@1") is False


def test_password_with_lowercase_is_valid():
    assert has_lowercase("Password@1") is True


# -------------------------
# Special character rule
# -------------------------

def test_password_without_special_character_is_invalid():
    assert has_special_character("Password123") is False


def test_password_with_special_character_is_valid():
    assert has_special_character("Password@123") is True


# -------------------------
# No spaces rule
# -------------------------

def test_password_with_spaces_is_invalid():
    assert has_no_spaces("Pass word@1") is False


def test_password_without_spaces_is_valid():
    assert has_no_spaces("Password@1") is True
