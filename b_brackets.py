def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    opener_set = ['(', '{', '[', '<']
    closer_set = [')', '}', ']', '>']
    bracket_stack = []

    for char in phrase:
        if char in opener_set:
            bracket_stack.append(char)
        elif char in closer_set:
            if not bracket_stack:
                return False
            else:
                past_bracket = bracket_stack.pop()
                index = opener_set.index(past_bracket)
                if closer_set[index] != char:
                    return False
                #else past_bracket==char, good!
        #else letter (don't care)
    if not bracket_stack:
        return True
    else:
        return False


ans = has_balanced_brackets("<ok>")
print("My result: ", ans, " Correct result: ", "True")

ans = has_balanced_brackets("<[ok]>")
print("My result: ", ans, " Correct result: ", "True")

ans = has_balanced_brackets("<[{(yay)}]>")
print("My result: ", ans, " Correct result: ", "True")

ans = has_balanced_brackets("(Oops!){")
print("My result: ", ans, " Correct result: ", "False")

ans = has_balanced_brackets("{[[This has too many open square brackets.]}")
print("My result: ", ans, " Correct result: ", "False")

ans = has_balanced_brackets(">")
print("My result: ", ans, " Correct result: ", "False")

ans = has_balanced_brackets("(This has {too many} ) closers. )")
print("My result: ", ans, " Correct result: ", "False")

ans = has_balanced_brackets("<{Not Ok>}")
print("My result: ", ans, " Correct result: ", "False")

ans = has_balanced_brackets("No brackets here!")
print("My result: ", ans, " Correct result: ", "True")