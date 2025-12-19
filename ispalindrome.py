def is_palindrome(s):
    return s == s[::-1]

s = input('enter a string: ')
is_palindrome(s)