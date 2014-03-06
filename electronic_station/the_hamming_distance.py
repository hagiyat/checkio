def checkio(n, m):
    return list(bin(n^m)).count('1')

if __name__ == '__main__':
    assert checkio(117, 17) == 3
    assert checkio(1, 2) == 2
    assert checkio(16, 15) == 5
