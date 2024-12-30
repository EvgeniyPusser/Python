def count_digits(number):
    count = 0
    while number > 0:
        # print(number%10)
        number = number // 10
        count += 1
    print("Number of figure in your number is:", count)


def search_digit(number, digit):
    res = False
    while number > 0:
        # print(number%10)
        if digit == number % 10:
            res = True
        number = number // 10
    return res, 45, 45


r = search_digit(678, 7)
print(r)
print(type(r))
print(search_digit(2341, 3))
