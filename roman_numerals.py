"""
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
"""
def checkio(data):
    result = ''
    roman = [(1000,'M'), (100,'C'), (10,'X'), (1,'I')]
    roman5 = [(500,'D'), (50,'L'), (5,'V')]
    for (index, (base,letter)) in enumerate(roman):
        tmp = data // base
        if tmp == 9:
            result += letter+roman[index-1][1]
        elif tmp >= 5:
            result += roman5[index-1][1]+letter*(tmp%5)
        elif tmp >= 4:
            result += letter+roman5[index-1][1]
        else:
            result += letter*tmp
        data = data % base

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'IV', '4'
    assert checkio(6) == 'VI', '6'
    assert checkio(9) == 'IX', '9'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
