import random


def is_positive(number):
    if number >= 0:
        print(number, "positive")
    else:
        print(number, "negative")


def is_even_and_negative(number):
    if number < 0 and number % 2 == 0:
        print(number, "Yes")
    else:
        print(number, "No")


def fan(number):
    if number == 0:
        print(number, "Switched off")
    if number == 1:
        print(number, "Speed 1")
    if number == 2:
        print(number, "Speed 2")
    if number == 3:
        print(number, "Turbo mode")
    if number != 0 and number != 1 and number != 2 and number != 3:
        print(number, "Error")


def my_age(age):
    if 0 <= age <= 17:
        print("child")
    if 17 < age < 67:
        print("adult")
    if 67 <= age:
        print("Senior")


is_positive(78)
is_positive(-78)
is_positive(0)

is_even_and_negative(-7)
is_even_and_negative(-90)
is_even_and_negative(77)

fan(random.randint(0, 5))
# fan(1)
# fan(3)

years = float(input("Enter your age"))
my_age(years)

a = 4
b = 5
c = a + b
print((c % 2 == 1) ^ (c == 9))






