def greater_subseqence(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


A = [1, 2, 6, 4, 4, 5, 0, 5]
B = [1, 2, 3, 6, 5, 6, 6, 4, 4, 5, 1, 2, 1]

h = greater_subseqence(A, B)
print(h)
