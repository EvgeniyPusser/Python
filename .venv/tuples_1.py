r = ("ui", 78)
print(type(r))

def divide(x, y):
    quotient = x//y
    remainder = x % y
    return (quotient, remainder)


o = divide(89, 7)
print(o[0], o[1])

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums =nums + (t[0],)
        if t[1] not in words:
            words=words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

E = ((1, "Hi"), (800, "Hi"), (9, "op"))

print(get_data(E))
print(type((6,)))

i = (2,2,2,2)
print(i)
