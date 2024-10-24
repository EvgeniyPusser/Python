def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(9))
n = 90
Fib = [0, 1] + [0]*(n-1)
for i in range(2, n + 1):
    Fib[i] = Fib[i-1] + Fib[i - 2]
print(Fib[n])


def traj_num(n):
    K = [0, 1] + [0] * n
    for i in range(2, n + 1):
        K[i] = K[i-2] + K[i -1]
    return K[n]

"""
Forbid some points"""
def traj_num(n):
    K = [0, 1] + [0] * n
    for i in range(2, n + 1):
        K[i] = K[i-2] + K[i -1]
    return K[2]


