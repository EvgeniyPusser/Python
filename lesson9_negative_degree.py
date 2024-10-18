def negative_degree(number, power: int):
    res = 1 / number
    while power < -1:
        res = res / number
        power += 1
    return res


# print(negative_degree(2, -3))


def n_p(x, y):
    sign = True
    if x == 0:
        return 0
    res = 1
    if y < 0:
        y = -y
        sign = False

    while y > 0:
        res = res * x
        y -= 1

    if sign:
        return res
    else:
        return 1 / res








print(n_p(3, 3))
