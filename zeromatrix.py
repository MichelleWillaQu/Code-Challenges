"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
    num_rows = len(matrix)
    num_column = len(matrix[0])

    column_idx_set = set()
    row_idx_set = set()

    for row_idx, n in enumerate(matrix):
        for column_idx, m in enumerate(n):
            if m == 0:
                column_idx_set.add(column_idx)
                row_idx_set.add(row_idx)


    for row_idx in row_idx_set:
        for column_idx in range(num_column):
            matrix[row_idx][column_idx] = 0
    for column_idx in column_idx_set:
        for row_idx in range(num_rows):
            matrix[row_idx][column_idx] = 0

    return matrix



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
