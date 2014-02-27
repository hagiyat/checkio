def checkio(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += " Buzz"
    return result.strip() if len(result) > 0 else str(number)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(5) == "Buzz"
    assert checkio(7) == "7"
