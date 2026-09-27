"""This module provides utility functions for string manipulation, including reversing a string, counting vowels, checking for palindromes, removing spaces, and counting words."""
text = input("Enter a string to reverse: ")
"""This is a reverse string function that takes a string as input and returns the reversed version of the string."""
reverse_string = lambda text: text[::-1]
"""This is a function that counts the number of vowels in a string."""
count_vowels = lambda text: sum(1 for char in text.lower() if char in 'aeiou')
"""This is a function that checks if a string is a palindrome."""
is_palindrome = lambda text: text.lower() == text.lower()[::-1]
"""This is a function that removes all spaces from a string."""
remove_spaces = lambda text: text.replace(" ", "")
"""This is a function that counts the number of words in a string."""
word_count = lambda text: len(text.split())
if __name__ == "__main__":
    print("Reversed string:", reverse_string(text))
    print("Number of vowels:", count_vowels(text))
    print("Is palindrome:", is_palindrome(text))
    print("String without spaces:", remove_spaces(text))
    print("Word count:", word_count(text))