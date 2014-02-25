import re
def checkio(data):
    src = ''.join(sorted(list(data)))
    return len(data) >= 10 and re.search(r'([0-9]+[A-Z]+[a-z]+)', src) != None


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('ULFFunH8ni') == True, "6th example"
