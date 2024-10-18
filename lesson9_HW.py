"""1. has_digit(сколько раз заданная цифра встречается в числе 34564534 цифра 4
встречается 3 раза) число положительное и отрицательное
2. print number reverse 345 -> 543 for positive and negative
3. сумма цифр
4. 345 целое но неотрицательное  напечатать цифры в столбик

"""


def has_digit(number, digit):
    if number < 0:
        number = - number
    counter = 0
    while number > 0:
        if digit == number % 10:
            counter += 1
        number = number // 10
    return counter


def reverse(number):
    if number == 0:
        print(0)
    if number < 0:
        print("-", end="")
        number = -number

    while number > 0:
        print(number % 10, end="")
        number = number // 10


def digit_sum(number):
    res = 0
    if number < 0:
        number = -number
    while number > 0:
        res = res + number % 10
        number = number // 10
    return res


def digit_column(number):
    if number >= 0:
        degree = len(str(number)) - 1
        while degree >= 0:
            print(number // 10 ** degree)
            number = number % (10 ** degree)
            degree -= 1


def digit_column2(number):
    number1 = number
    count = -1
    while number > 0:
        number = number // 10
        count += 1
    while count > -1:
        print(number1 // (10 ** count))
        number1 = number1 % (10 ** count)
        count -= 1


print("Your digit in the number can be found", has_digit(57866666, 6), "times")
print("In reverse your number looks like that: ", end="")
reverse(456723)
print("\nSum of digits for the following number is: ", digit_sum(9876))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Two variants of printing in column the digits: ")
print("First, using string formatting: ")
digit_column(8978)
print("Second, what we know now using only: ")
digit_column2(8978)
