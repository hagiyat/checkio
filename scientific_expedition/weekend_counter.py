from datetime import date
def checkio(from_date, to_date):
    diff = (to_date - from_date).days + 1
    # 先頭週と末尾週の分で+2
    days = ((list(range(7))*(diff//7+2))[from_date.weekday():])[0:diff]
    return days.count(5) + days.count(6)


if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2
