import re
def checkio(data):
    counter = {}
    for letter in list(re.sub(r'[^a-z]', '', data.lower())):
        counter[letter] = counter.get(letter, 0) + 1
    result = [key for key,value in counter.items() if value > 1 and value >= max(counter.values())]

    return sorted(result)[0] if result else list(data)[-1]

if __name__ == '__main__':
    assert(checkio("Hello World!") == "l")
    assert(checkio("How do you do?") == "o")
    assert(checkio("One") == "e")
    assert(checkio("Oops!") == "o")
    assert(checkio("AAaooo!!!!") == "a")
    assert(checkio("Lorem ipsum dolor sit amet") == "m")
