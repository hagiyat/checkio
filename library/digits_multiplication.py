def checkio(number):
    result = 1 if number > 0 else 0
    for value in [value for value in getDigits(number) if value > 0]:
        result *= value
    return result

def getDigits(data):
    while data > 1:
        yield data % 10
        data //= 10

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(0) == 0
    assert checkio(1111) == 1
