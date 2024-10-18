import random


def is_even_or_odd(number: int):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# ri = random.randint(2, 400)
is_even_or_odd(random.randint(2, 400))


def is_odd_and_positive(number: int):
    if number % 2 != 0 and number > 0:
        print("yes")
    else:
        print("no")


is_odd_and_positive(456)


# David - 1 Haim - 2 Hanna - 3 Eden - 4

def taxi(code: int):
    if code == 1:
        print("David, go!")
    if code == 2:
        print("Haim, go!")
    if code == 3:
        print("Hanna, go!")
    if code == 4:
        print("Eden, go!")
    if code < 1 or code > 4:
        print("Error")


taxi(random.randint(1,5))

# HW 1.function -> is_positiv (number):
# if number  >= 0 print "positiv"
# else "negative"
"""
2. is_even_and_negative "yes" "no"

3. fan(mode: int)
mode == 0 "Switched off"
== 1 "Speed 1"
== 2 "Speed 2"
== 3 "Turbo mode"
"Error"

4. my_age(age) 
if age from [0 to 17] "child"
from (17 to 67) "adult"
[67..."senior"
"""

print(45**2)

