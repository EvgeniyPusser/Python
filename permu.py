def find(number, A):
    # ищет number ив А и возвращает Правда, если есть ,и ЛОжь, если нет
    for x in A:
        if number == x:
            return True
    return False


def gen_permutation(N, M=-1, prefix=None, counte=0):
    """Генерирует перестановки N чисел в M позициях с префиксом

    :param counte:
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    M = N if M == -1 else M
    # по умолчанию N чисел в N позициях
    prefix = prefix or []

    if M == 0:
        print(*prefix, end=", ", sep="")
        return counte + 1
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        # print(prefix)
        prefix.append(number)
        counte = gen_permutation(N, M - 1, prefix, counte)
        prefix.pop()

    return counte


io = gen_permutation(5)
print("\nPermutation amount is: ",  io)
