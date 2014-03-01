"""
import re
def checkio(words_set):
    for word in words_set:
        for target in [target for target in words_set if target != word]:
            if re.search(r'' + word + '$', target):
                return True

    return False
"""
def checkio(words_set):
    for word, target in [(word, target)
            for word in words_set
            for target in words_set if word != target]:
        if word.endswith(target):
            return True

    return False


if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True
    assert checkio({"hello", "la", "hellow", "cow"}) == False
    assert checkio({"walk", "duckwalk"}) == True
    assert checkio({"one"}) == False
    assert checkio({"helicopter", "li", "he"}) == False
