import Fuctions


def hello_separeted(name="World", separator="-"):
    print("Hello,", name, "everywhere", sep=separator)


hello_separeted(separator=" && ",
                name="John")

print(Fuctions.is_simple_number(733))
# help(help(Functions.is_simple_number))
Fuctions.number_divisers(23456)
Fuctions.factorize_number(628)
