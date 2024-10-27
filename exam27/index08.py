# 9) Prime time (4 ქულა)

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def prime(x):
    y = []
    z = []
    for i in range(1, x+1):
        if i % 1 == 0 and i % i == 0 and i % 4 != 0 and i % 3 != 0 and i % 10 != 0 and i % 2 != 0:
            z.append(i)
        else:
            y.append(i)
    z[0] = 2
    return z

print(prime(119))