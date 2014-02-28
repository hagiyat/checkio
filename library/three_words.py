def checkio(words):
    counter= 0
    for word in words.split(" "):
        if word.isalpha() == True:
            counter += 1
            if counter >= 3:
                return True
        else:
            counter = 0

    return False

if __name__ == '__main__':
    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False
    assert checkio("one two 3 four 5 six 7 eight 9 ten eleven 12") == False
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True

