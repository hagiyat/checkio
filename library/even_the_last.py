def checkio(array):
    if len(array) < 1:
        return 0
    result = [(array[index]) for index,value in enumerate(array) if index % 2 == 0]
    return sum(result) * array[-1]

if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30
    assert checkio([1, 3, 5]) == 30
    assert checkio([6]) == 36
    assert checkio([]) == 0
