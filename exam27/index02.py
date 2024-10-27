# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

def removing_duplicates(z):
    k = []
    for i in z:
        if i not in k:
            k.append(i)
    

    return k

print(removing_duplicates([1,2,2,3,4,4,5]))

'''
not in მე თვითონ ვისწავლე პროექტის გაკეთებისას!
'''