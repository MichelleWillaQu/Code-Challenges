"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    one_error = False
    shifting = False

    if abs(len(w1) - len(w2)) > 1:
        return False

    if len(w1) != len(w2):
        shifting = True

    shorter_word = w2 if (len(w1) > len(w2)) else w1
    longer_word = w1 if (len(w1) > len(w2)) else w2

    idx2 = 0
    for idx, letter in enumerate(shorter_word):
        if letter != longer_word[idx2]:
            if one_error:
                return False
            if letter == longer_word[idx2 + 1] and shifting:
                idx2 += 1
            one_error = True
        idx2 += 1
    return True



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
