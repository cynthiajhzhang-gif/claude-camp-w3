import pytest
from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single():
    assert reverse_words("hello") == "hello"

def test_reverse_words_empty():
    assert reverse_words("") == ""

def test_count_vowels_normal():
    assert count_vowels("hello") == 2

def test_count_vowels_uppercase():
    assert count_vowels("HELLO") == 2

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0

def test_count_vowels_invalid():
    with pytest.raises(TypeError):
        count_vowels(123)

def test_is_palindrome_true():
    assert is_palindrome("racecar") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_spaces():
    assert is_palindrome("race car") == True

def test_is_palindrome_invalid():
    with pytest.raises(TypeError):
        is_palindrome(123)