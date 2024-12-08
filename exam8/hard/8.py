# Problem 8: Longest Consecutive Sequence - 8ქ
# Challenge:
#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Instructions:
# Input: A list of integers (e.g., [100, 4, 200, 1, 3, 2]).
# Output: The length of the longest consecutive sequence (e.g., 4).
# Test Cases:
# assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
# assert longest_consecutive([0, 0]) == 1
# assert longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9

def longest_sequence(l):
    x = []
    for i in range(1, max(l)+1):
        x.append(i)
        if x[-2] != x[-1]:
            return
    return x
print(longest_sequence([2, 20]))