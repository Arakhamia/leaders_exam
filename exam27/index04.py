# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def palindrome(x):
    z = x.lower()
    y = z.split(" ")
    w = "".join(y)

    if w == w[::-1]:
        return True
    else:
        return False

print(palindrome("A man a plan a canal Panama"))