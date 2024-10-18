import random


def get_number(num, nom, yu):
    q = (num * nom + yu) + random.randint(23, 70)
    t = (q * 78) % 41
    return t


res = get_number(10, 67, 3)
print("res =", res)


def half(e):
    return (e / 2) + get_number(2, 4, 5)


# print("Res = ", input("Enter number"), half(input()))
