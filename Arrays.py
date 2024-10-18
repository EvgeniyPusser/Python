import random

# A = [1, 2, 3, 11, 6]
# print(A)
#
# for x in A:
#     x *= x
#     print(x)
#
# print(type(A))
# A[0] = 5
# print(A)
#
# for u in range(len(A)):
#     A[u] *= A[u]
# print(A)

I = [0] * 11
top = 0
# print(I)
x = int(random.randint(9, 89))
while x != 2:
    I[top] = x
    top += 1
    x = int(random.randint(-1, 11))
for k in range(2, -1, -1):
    print(I[k], end=" ")
C = I
print(C)