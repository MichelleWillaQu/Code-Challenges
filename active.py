"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active
1951-1960. Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    start_dict = {}
    end_dict = {}
    # Brute force
    for name, start, end in bio_data:
        # Init
        start_dict[start] = 0
        end_dict[end] = 0
    for key in start_dict:
        # Count
        for name, start, end in bio_data:
            if start < key and end > key:
                start_dict[key] = start_dict.get(key) + 1
    for key in end_dict:
        # Count
        for name, start, end in bio_data:
            if start < key and end > key:
                end_dict[key] = end_dict.get(key) + 1
    # Loop to get start
    max = 0
    start_period = 1999
    for key in start_dict:
        if start_dict[key] > max:
            start_period = key
            max = start_dict[key]
        elif start_dict[key] == max:
            if start_period > key:
                start_period = key
                max = start_dict[key]
    end_period = 1999
    for key in end_dict:
        if key > start_period:
            if end_dict[key] == max:
                if key < end_period:
                    end_period = key
    time_period = (start_period, end_period)
    return time_period


# The optimal solution is to have a list of the each year in the century so
# there does not have to be any double loop over n - this is technically O(n)
# as well because each dict cannot have more than 100 keys but it is less
# readable for sure

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
