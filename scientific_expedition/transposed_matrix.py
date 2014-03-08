def checkio(data):
    """
    result = []
    for h in range(0, len(data[0])):
        result.append([data[v][h] for v in range(0, len(data))])
    return result
    """
    print([e for e in zip(*data)])
    return [list(e) for e in zip(*data)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 2, 3],
                    [4, 5, 6]]) == [[1, 4],
                                    [2, 5],
                                    [3, 6]], "Rectangle matrix2"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"


