import random
from collections import defaultdict


def Counting_sort(A, mn, mx):
    count = defaultdict(int)
    for i in A:
        count[i] += 1
    result = []
    # print(A)

    for j in range(mn, mx + 1):
        result += [j] * count[j]

    return result


A = [0] * 10
for a in range(10):
    A[a] = random.randint(1, 9)
r = Counting_sort(A, min(A), max(A))
print(r)

A = [1, 2, 2, 3, 3, 3, 4]
count = defaultdict(int)
print(count)

result = []  # result is empty: []
result.append(2)
result.append(3)

print(result)


