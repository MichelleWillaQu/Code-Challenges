"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letters_dict = {}
    for char in word:
        letters_dict[char] = letters_dict.get(char, 0) + 1

    if len(word) % 2 == 0:
        #even number so must have letters in multiples
        for letter in letters_dict:
            if letters_dict[letter] % 2 != 0:
                return False
    else:
        singular_letter_found = False
        for letter in letters_dict:
            if letters_dict[letter] % 2 != 0:
                if singular_letter_found:
                    return False
                else:
                    singular_letter_found = True
    return True



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
