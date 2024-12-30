# def salary():
#     hours = float(input("Enter hours"))
#     wage = float(input("Enter wage"))
#     tax = float(input("Enter tax"))
#     brutto = hours * wage
#     tax_money = brutto * tax / 100
#     return brutto - tax_money
#
#
# def done(a1, a2, a3):
#     return a1 + a2 - a3
#
#
# def read():
#     return float(input("Enter a"))
#
#
# print(done(read(),read(),read()))


"""HW

First 

def subtract(num1, num2):
return -

divide 
:
Второе

папа собрал 4.5 кг яблок
Сара собрала 5.5. кг
дети девочка Эден 1.5 кг и мальчик Давид собрал 2 кг

высыпали в той очередности в которой они тут
распечатать все и корзинку
Total in basket kg
Average per person

Третье

функция , которая exchange полкчает шекели, курс и комиссию
для долларов и для евро

"""


# First task

def subtract(n1, n2):
    return n1 - n2


def dev(n1, n2):
    return n1 / n2


print(subtract(78, 7))
print(dev(789, 5))


# Second task


def papa():
    return 4.5


def sara():
    return 5.5


def eden():
    return 1.5


def david():
    return 2


basket = papa()
print(f"{basket: .3f} kg")

basket = basket + sara()
print(f"{basket: .3f} kg")

basket = basket + eden()
print(f"{basket: .3f} kg")

basket = basket + david()
print(f"Total amount: {basket: .3f} kg")

print(f"Average per person: {basket / 4: .3f} kg")


# Third task

def change_dollars(amount, rate, commission):
    dollars = amount / rate
    com = dollars * commission / 100
    res = dollars - com
    return res

try:
    ratedoll = float(input("Enter rate of $"))
    print(f"Your cash is: {change_dollars(1000, ratedoll, 2): .2f} $ ")
except:
    print("Bug in user input")



def change_euros(amount, rate, commission):
    euros = amount / rate
    com = euros * commission / 100
    res = euros - com
    return res


erat = float(input("Enter euros rate"))
print(f"Your cash is: {change_euros(1000, erat, 2): .2f} Euros")

