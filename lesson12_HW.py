"""
1.negative_count(A)
2.evens_positive_sum(A)
3.search_max(A)
4.search_min_positiv


"""


def negative_count(A):
    count = 0
    for i in A:
        if i < 0:
            count += 1
    return (count)


def evens_positiv_sum(A):
    sum_of = 0
    for i in A:
        if i >= 0:
            sum_of += i
    return sum_of


def search_max(A):
    max = A[0]
    for i in A:
        if i > max:
            max = i
    return max


def search_min_positive(A):
    min_p = 0
    for i in A:
        if i >= 0:
            min_p = i
            break

    for i in A:
        if min_p >= i >= 0:
            min_p = i
    return min_p


A = [-3, -8, -20, 5, 56, 7]
print("Колличество отрицательных чисел равно: ", negative_count(A))
print("Сумма положительных чисел равна: ", evens_positiv_sum(A))
print("Максимум равен: ", search_max(A))
print("минимальное положительное число равно: ", search_min_positive(A))
