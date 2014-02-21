import re
def checkio(data):
    #return len(data) >= 10 and re.search(r'([A-Z]+[a-z]+[0-9]+)', data) != None
    if len(data) < 10:
        return False
    if re.search(r'[A-Z]+', data) == None:
        return False
    if re.search(r'[a-z]+', data) == None:
        return False
    if re.search(r'[0-9]+', data) == None:
        return False

    return True


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('ULFFunH8ni') == True, "6th example"
