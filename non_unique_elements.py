def checkio(src):
    matched = []
    result = []

    # ループ二重とかどうにかならないものか・・・
    for index, value in enumerate(src):
        if value in src[index+1:]:
            matched.append(value)

    for value in src:
        if value in matched:
            result.append(value)

    return result



if checkio([1, 3, 1, 3, 2]) == [1, 3, 1, 3]:
    print "Done!"
