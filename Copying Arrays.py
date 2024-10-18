
N = int(input())
A = [4] * N
B = [0]* N
C = A
for k in range(N):
    C[k] = A[k] + 8
print(C)
C[1] = 8
print(A)

L = list(C)
print(L)

