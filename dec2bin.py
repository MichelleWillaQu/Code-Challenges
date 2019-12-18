"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

And finally, using division:

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'


"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""
    binary = []
    if num == 0:
        return '0'
    while num != 1:
        if num % 2 == 1:
            binary.append('1')
        else:
            binary.append('0')
        num = num // 2
    binary.append('1')
    return ''.join(binary[::-1])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
