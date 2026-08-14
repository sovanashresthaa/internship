# Write a function to check whether a string is a palindrome.

def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")