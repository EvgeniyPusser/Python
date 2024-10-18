# noinspection PyInterpreter
def eratosthen_sieve():
    N = int(input())
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2 * k, N, k):
                A[m] = False
    for k in range(N//2):
        print(k, "- ", "simple" if A[k] else "compound", end=" ;\n")
    for k in range(N//2, N):
        print("\t", k, "- ", "simple" if A[k] else "compound", end=" ;\n")


# M = int(input())
# C = [True] * M
# C[0]= C[1] = False
# for i in range(2, M):2
#     if C[i]:
#         for i in range(2*i, M, i):
#             C[i] = False
# for i in range(M):
#     print(i, "- ", "simple" if C[i] else "compound", end=" ;\n")


eratosthen_sieve()

