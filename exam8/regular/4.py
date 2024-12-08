# Problem 4: Longest Substring Without Repeating Characters - 5ქ
# Challenge:
#  Create a function that finds the length of the longest substring without repeating characters.
# Instructions:
# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").
# Test Cases:
# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3

def sub(s):
    x = []
    y = []
    for i in s:
        if i not in x:
            x.append(i)
        elif i in x:
            y.append(i)
            
    return len(x)

print(sub("bbb"))

#not in-არ არის x-ში
#in-არის x-ში