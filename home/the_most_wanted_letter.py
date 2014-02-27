import re
def checkio(data):
    data = list(re.sub(r'[^a-z]', '', data.lower()))
    counter = {}
    for letter in data:
        counter[letter] = counter.get(letter, 0) + 1
    result = [key for key,value in counter.items() if value > 1 and value >= max(counter.values())]

    return sorted(result)[0] if result else sorted(data)[0]

if __name__ == '__main__':
    assert(checkio("Hello World!") == "l")
    assert(checkio("How do you do?") == "o")
    assert(checkio("One") == "e")
    assert(checkio("Oops!") == "o")
    assert(checkio("AAaooo!!!!") == "a")
    assert(checkio("Lorem ipsum dolor sit amet") == "m")
    assert checkio("abe") == "a"
