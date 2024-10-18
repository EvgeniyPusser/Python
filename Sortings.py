def insert_sort(A):
    """
    соритировка списка А вставками
    :param A:
    :return:
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choice_sort(A):
    """
    сортировка списка А выбором
    :param A:
    :return:
    """
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """
    сорртировка списка А методом пузырька
    :param A:
    :return:
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def test_sort(sort_algorithm):
    print("we are testing ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    if A == A_sorted:
        print("OK")
    else:
        print("Fail")
    print("testcase #1: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    if A == A_sorted:
        print("OK")
    else:
        print("Fail")
    print("testcase #1: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    if A == A_sorted:
        print("OK")
    else:
        print("Fail")


print(list(range(10, 20)))
test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)


def sorting_count(A):
    N = 10
    F = [0] * 10
    for i in range(N):
        x = int(input())
        F[x] += 1


print(sorting_count({1,3,2,2,2,2,5,8}))
