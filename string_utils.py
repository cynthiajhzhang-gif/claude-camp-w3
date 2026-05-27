def reverse_words(s):
    """反转单词顺序"""
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")
    words = s.split()
    words = words[::-1]
    return " ".join(words)

def count_vowels(s):
    """统计元音字母数量"""
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")
    s = s.lower()
    count = 0
    for char in s:
        if char in "aeiou":
            count += 1
    return count

def is_palindrome(s):
    """判断是否回文"""
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")
    s = s.lower().replace(" ", "")
    return s == s[::-1]