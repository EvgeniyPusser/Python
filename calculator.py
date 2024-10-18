def calculator(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        if number2 != 0:
            return number1 / number2
        else:
            print("ERROR : division by ZERO")
    elif sign == "**":
        return number1 ** number2
    else:
        print("wrong action")


n1 = float(input("Enter number1 "))
n2 = float(input("Enter number2 "))
what_to_do = input("Enter sign (+,-,*, /, ** >>> ")

r = calculator(n1, n2, what_to_do)


if r is not None:
    print("Everything is ok")
    print(f"{r: .3f}")