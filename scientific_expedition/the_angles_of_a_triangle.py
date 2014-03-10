import math
def checkio(a, b, c):
    try:
        result = [arccos(a, b, c), arccos(b, c, a), arccos(c, a, b)]
        return sorted(result)
    except:
        return [0, 0, 0]


def arccos(a, b, c):
    radian = math.acos((b**2 + c**2 - a**2) / (2*b*c))
    if radian == 0.0:
        raise ValueError()
    return round(math.degrees(radian))

"""
find_angle = lambda s1, s2, so: int(round(
        degrees(acos((s1 ** 2 + s2 ** 2 - so ** 2) / (2 * s1 * s2))), 0))
"""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10, 20, 30) == [0, 0, 0]
    assert checkio(30, 20, 10) == [0, 0, 0]
    assert checkio(4, 4, 4) == [60, 60, 60]
    assert checkio(3, 4, 5) == [37, 53, 90]
    assert checkio(2, 2, 5) == [0, 0, 0]
