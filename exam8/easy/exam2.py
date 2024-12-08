# Problem 2: Sum of Positive Numbers with Flooring - 2ქ
# Challenge:
#  Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.
# Instructions:
# Input: A list of numbers, which may include fractions (e.g., [1, -4, 7, 12] or [-1.5, 2.7, -3.3, 4.8]).
# Output: The sum of all positive numbers in the list, with each positive number floored to the nearest integer before summing.
# Test Cases:
# assert problem_2_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6  # floor(2.7) + floor(4.8) = 6
# assert problem_2_sum_of_positive([]) == 0
# assert problem_2_sum_of_positive([-1, -2, -3]) == 0


#შემოვიტანე ბიბლიოთეკა რომლის დახმარებითაც შემიძლია რთული მათემატიკური ოპერაციების შესრულება.
from math import * 


def sum_of_positives(list):
    x = []
    y = []
    for i in list:
        if i > 0:
            x.append(floor(i))
            # floor-ის ნაცვლად შეიძლება გამოვიყენოთ int, ორივეს ათწილადი გადაყვას უმცირეს-უახლოეს ერთეულამდე
        elif i <= 0:
            y.append(i)
            
    return sum(x)

print(sum_of_positives([2, 4, 14, 3.4, -1, 6.8]))