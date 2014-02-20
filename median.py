def checkio(data):
    src = sorted(data)
    if len(data) % 2 == 1:
        median = src[(len(data)-1) >> 1]
    else:
        center = len(data) >> 1
        median = (src[center-1]+src[center]) / 2

    return median



assert(checkio([1, 2, 3, 4, 5]) == 3)
assert(checkio([3, 1, 2, 5, 3]) == 3)
assert(checkio([1, 300, 2, 200, 1]) == 2)
assert(checkio([3, 6, 20, 99, 10, 15]) == 12.5)
