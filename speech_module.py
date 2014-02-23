FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(data):
    words = [""]+FIRST_TEN+SECOND_TEN
    for word in [(high+' '+low) for high in OTHER_TENS for low in [""]+FIRST_TEN]:
        words.append(word.strip())

    result = []
    if data >= 100:
        result.append(words[data//100])
        result.append(HUNDRED)
        data %= 100
    result.append(words[data])

    return ' '.join(result).strip()



if __name__ == '__main__':
    assert(checkio(4)=='four')
    assert(checkio(143)=='one hundred forty three')
    assert(checkio(12)=='twelve')
    assert(checkio(101)=='one hundred one')
    assert(checkio(212)=='two hundred twelve')
    assert(checkio(40)=='forty')
    assert(checkio(100)=='one hundred')
