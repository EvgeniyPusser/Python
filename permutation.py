def generate_numbers(N, M, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    # prefix = prefix or []
    # print(prefix)
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        #print(prefix)
        #prefix.pop()
        #print(i)
        #print(prefix, end="!!")


def gen_bin(M, pref=""):
    if M == 0:
        print(pref)
    else:
        gen_bin(M - 1, pref + "o")
        print(pref)
        gen_bin(M - 1, pref + "2")
        print(pref)


def gen_bin_arr(M, pref="", result=None):
    if result is None:
        result = []

    if M == 0:
        result.append(pref)
    else:
        gen_bin_arr(M - 1, pref + "o", result)
        gen_bin_arr(M - 1, pref + "2", result)

    return result


# Example usage
print(gen_bin(3))

#
print(generate_numbers(3, 3))
gen_bin(2)
print(gen_bin_arr(2))
