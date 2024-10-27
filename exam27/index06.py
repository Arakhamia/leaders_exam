# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def fibonacci(x):
    y = []
    for i in range(2):
        y.append(i)

    for i in range(x-2):
        y.append(y[-1] + y[-2])

    return y

print(fibonacci(7))