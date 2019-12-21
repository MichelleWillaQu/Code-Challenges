"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    # max_count = 1
    # count = 1
    # letters_dict = {}
    # most_anagrams_word = ""
    # letters_dict_list = []
    # for word in wordlist:
    #     for letter in word:
    #         letters_dict[letter] = letters_dict.get('letter', 0) + 1
    #     letters_dict_list.append(sorted(list(letters_dict.items())))
    #     letters_dict = {}

    # cutting_wordlist = wordlist[:]
    # to_cut_idx = []
    # seen = set()
    # while wordlist:
    #     word = wordlist.pop(0)
    #     cutting_wordlist.pop(0)
    #     letters_dict = letters_dict_list.pop(0)
    #     seen.add(word)
    #     for idx, next_word in enumerate(wordlist):
    #         if next_word in seen:
    #             to_cut_idx.append(idx)
    #             cutting_wordlist.remove(next_word)
    #         elif len(next_word) == len(word):
    #             if letters_dict_list[idx] == letters_dict:
    #                 seen.add(next_word)
    #                 to_cut_idx.append(idx)
    #                 count += 1
    #                 cutting_wordlist.remove(next_word)

    #     if count > max_count:
    #         most_anagrams_word = word
    #         max_count = count
    #     wordlist = cutting_wordlist[:]
    #     if to_cut_idx:
    #         for idx in reversed(to_cut_idx):
    #             letters_dict_list.pop(idx)
    #     # if word == 'angor':
    #     #     print('COUNT: ', count)
    #     count = 1
    #     to_cut_idx = []
    # print('MAX: ', max_count)
    # return most_anagrams_word
    
    combo_dict = {}
    for word in wordlist:
        sorted_chars = ''.join(sorted(word))
        if combo_dict.get(sorted_chars):
            combo_dict[sorted_chars].append(word)
        else:
            combo_dict[sorted_chars] = [word]

    max_count = 0
    word_thats_max = ''
    for key in combo_dict:
        if len(combo_dict[key]) > max_count:
            max_count = len(combo_dict[key])
            word_thats_max = combo_dict[key][0]

    return word_thats_max




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
