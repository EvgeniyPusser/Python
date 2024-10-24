def hoar_sort(A, ascend=True):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    s = 2 * int(ascend) - 1
    for x in A:
        if s * x < s * barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
            hoar_sort(L)
            hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


A = [44, 3, 0.3, 222, 9]
hoar_sort(A, False)
print(A)


def check_sorted(A, ascending=False):
    """
    Проверка отсортированности за О(len(A))
    :param A:
    :param ascending:
    :return:
    """
    N = len(A)
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, N - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


print(check_sorted(A))
