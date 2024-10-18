# alex   25
# hanna 35.50
# igor 120
# edna 154.60

def alex():
    return 25


def hanna():
    return 35.50


def igor():
    return 120


def edna():
    return 154.60


def sum():
    return alex() + hanna() + igor() + edna()


wallet = sum()
print(f"{wallet: .2f}")

wallet = alex()
print(f"in wallet: {wallet: .2f} NIS")

wallet = wallet + hanna()
print(f"in wallet: {wallet: .2f} NIS")

wallet = wallet + igor()
print(f"in wallet: {wallet: .2f} NIS")

wallet = wallet + edna()
print(f"Total in wallet: {wallet: .2f} NIS")

print(f"Average per person(NIS): {wallet / 4: .2f}")




