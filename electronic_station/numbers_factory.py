def checkio(number):
    quotients = []
    try:
        for value in getDivisors(number):
            quotients.append(str(value))
        return int("".join(reversed(quotients)))
    except:
        return 0

def getDivisors(number, divisor=9):
    while number > 1:
        if number % divisor == 0:
            yield divisor
            number //= divisor
            divisor = 9
        elif divisor > 2:
            divisor -= 1
        else:
            raise ValueError("invalid argument.")

"""
割り算しか頭になかったので、思わずうなった回答

def findmult(data):
    result = 1
    for c in str(data):
        result *= int(c)

    return result

def checkio(data):
    for  i in range(1, 1000000):
        if findmult(i) == data:
            return i

    return 0
"""


if __name__ == '__main__':
    assert checkio(64) == 88
    assert checkio(20) == 45
    assert checkio(21) == 37
    assert checkio(17) == 0
    assert checkio(33) == 0
