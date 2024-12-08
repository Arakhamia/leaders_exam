# Problem 7: 3Sum Problem - 8ქ
# Challenge:
#  Find all unique triplets in an array that sum up to zero.
# Instructions:
# Input: A list of integers (e.g., [-1, 0, 1, 2, -1, -4]).
# Output: A list of unique triplets that sum to zero.
# Test Cases:
# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert three_sum([1, 2, -2, -1]) == []

def zero(l):
    x = []
    y = []

    for i in l:
        if sum(x) == 0:
            y.append(i)
        elif sum(x) != 0:
            x.append(i)

    return y, x

print(zero([2, 4, 6, 3, 1]))