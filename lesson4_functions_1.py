# f1() -> word "name"
# f2     "My"
# f3      "is"
# f4   "Jenia"

# def f1():
#     print("\n\tname", end=" ")
#
#
# def f2():
#     print("My", end=" ")
#
#
# def f3():
#     print("\n\t\tis", end=" ")
#
#
# def f4():
#     print("\n\t\t\tJenia.", end="")
#
#
#
# def main():
#     f2()
#     f1()
#     f3()
#     f4()


#
# Первая
# 1. Запрашиваем с помощью инпута у пользователя Enter amount of NIS
# 2.Второй запрос инпут Enter dollar rate
# 3. Третий запрос инпут Enter commission in % обменника
# 4. Посчитать сколько положено на руки в долларах
# 5. инпут Enter euro
# 6. С учетом этой же комиссии распечатать скольок получается  вевро
#
# Вторая
# четыре функции
# f1() печатаем одно слово "be"
# f2() "to"
# f3() "not"
# f4() "or"
# main()"?"
# print("to be or not to be?")
#
# Третий
#
# print("to be
#              or not
#                     to be?")

# Первое задание

# amount = float(input("Enter the sum of money "))
# dollar_rate = float(input("Enter the dollar-NIS rate "))
# euro_rate = float(input("Enter the euro-NIS rate "))
# commission = float(input("Enter currency exchange commission in percent "))
# dollar_res = (amount / dollar_rate) - (amount / dollar_rate) * commission / 100
# euro_res = (amount / euro_rate) - (amount / euro_rate) * commission / 100
#
# print(f"Your money is {dollar_res: .2f} $")
# print(f"Your money is {euro_res: .2f} euros")
#
# print()


# Второе задание

def f1():
    print("be", end="")


def f2():
    print("to", end=" ")


def f3():
    print("not", end=" ")


def f4():
    print(" or", end=" ")


def main():
    f2()
    f1()
    f4()
    f3()
    f2()
    f1()
    print("?", end=" ")


main()
print()


# Третье задание
def f11():
    print("be", end="")


def f22():
    print("to", end=" ")


def f33():
    print("not\n\t\t\t", end=" ")


def f44():
    print("\n\t or", end=" ")


def main():
    f22()
    f11()
    f44()
    f33()
    f22()
    f11()
    print("?", end=" ")


main()


def igor():
    return 56.9999


wallet = igor()
print(wallet)

print(wallet)
