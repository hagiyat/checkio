def my_checkio(first, second):
    search = second.split(",")
    result = []
    for word in first.split(","):
        if word in search:
            result.append(word)
    return ",".join(sorted(result))


def checkio(first, second):
    result = set(first.split(",")).intersection(set(second.split(",")))
    return ",".join(sorted(result))

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
