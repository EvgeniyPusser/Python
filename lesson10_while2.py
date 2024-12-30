"""
1. odds digits count(number)
сколько нечетных цифр в числе

2. digits_sum(number)

3. evens_sum

4. max_digit



"""


def odds_counts(number: int):
    count = 0
    if number < 0:
        number = - number
    while number > 0:

        rem = number % 10
        if rem % 2 == 1:
            count += 1
        number = number // 10
    return count


def digits_sum(number: int):
    if number < 0:
        number = -number
    sum_dig = 0
    while number > 0:
        sum_dig = sum_dig + number % 10
        number //= 10
    return sum_dig


def evens_sum(number: int):
    if number < 0:
        number = -number
    sum_dig = 0
    while number > 0:
        if (number % 10) % 2 == 0:
            sum_dig = sum_dig + number % 10
        number //= 10
    return sum_dig


def max_dig(number: int):
    if number < 0:
        number = - number
    max_d = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > max_d:
            max_d = number % 10
        number = number//10
    return max_d








r = odds_counts(-9944)
print(r)
print((digits_sum(-22220)))
print(evens_sum(104))
print(max_dig(-0))
