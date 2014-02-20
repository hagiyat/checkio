def checkio(els):
    result = 0
    for value in els[0:3]:
        result += value

    return result

if checkio([1, 2, 3, 4, 5, 6]) == 6:
    print('Done!')
