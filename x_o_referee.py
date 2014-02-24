def checkio(game_result):
    src = []
    for line in [[(line[index]) for line in game_result] for index in range(0, 3)]:
        src.append("".join(line))
    src.append(''.join([(line[index]) for index,line in enumerate(game_result)]))
    src.append(''.join([(line[index]) for index,line in enumerate(reversed(game_result))]))

    if 'X'*3 in game_result+src:
        return 'X'
    elif 'O'*3 in game_result+src:
        return 'O'
    return 'D'


if __name__ == '__main__':
    assert(checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X") # "Xs wins"
    assert(checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O")
    assert(checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D")
