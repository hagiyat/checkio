def checkio(number):
    for (minutes, pegeons) in getPegeons():
        number -= sum(pegeons)
        if number <= 0:
            ajust = pegeons[-1] if number < 0 and abs(number) >= pegeons[-1] else -number
            return sum(pegeons) - ajust



def getPegeons():
    result = []
    for n in range(1,100000):
        result.append(n)
        yield n, result

if __name__ == '__main__':
    assert checkio(1) == 1
    assert checkio(2) == 1
    assert checkio(5) == 3
    assert checkio(10) == 6
    assert checkio(19) == 9
