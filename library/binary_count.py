def my_checkio(str_number, radix):
    letters = [str(i) for i in range(0, radix if radix < 10 else 10)]
    letters += [chr(i) for i in range(ord('A'), ord('A')+radix-10)]

    result = 0
    for index, value in enumerate(reversed(list(str_number))):
        if value not in letters:
            return -1
        result += letters.index(value) * (radix ** index)

    return result

def checkio(str_number, radix):
    try:
        r = int(str_number, radix)
    except ValueError:
        return -1

    return r

if __name__ == '__main__':
    assert checkio("AF", 16) == 175
    assert checkio("101", 2) == 5
    assert checkio("101", 5) == 26
    assert checkio("Z", 36) == 35
    assert checkio("AB", 10) == -1
