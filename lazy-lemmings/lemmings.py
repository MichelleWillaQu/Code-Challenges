"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # max_distance = 0
    # lemming_distance = None
    # for lemming in range(num_holes):
    #     for cafe in cafes:
    #         to_cafe_distance = abs(lemming - cafe)
    #         if lemming_distance == None or lemming_distance > to_cafe_distance:
    #             lemming_distance = to_cafe_distance
    #     if lemming_distance > max_distance:
    #         max_distance = lemming_distance
    #     lemming_distance = None
    # return max_distance


    # BINARY
    


def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    max_distance = 0
    lemming_distance = None
    if len(cafes) == 1:
        dist_to_end = num_holes - 1 - cafes[0]
        return dist_to_end if dist_to_end > cafes[0] else cafes[0]
    # If more than one
    # Because equal or less number of cafes to holes
    for idx, cafe in enumerate(cafes):
        if idx == 0:
            dist_to_right = (cafes[1] - cafe) // 2
            lemming_distance = dist_to_right if dist_to_right > cafe else cafe
        elif idx == len(cafes) - 1:
            dist_to_left = (cafe - cafes[idx - 1]) // 2
            dist_to_right = num_holes - 1 - cafe
            lemming_distance = dist_to_left if dist_to_right < dist_to_left else dist_to_right
        else:
            dist_to_left = (cafe - cafes[idx - 1]) // 2
            dist_to_right = (cafes[idx + 1] - cafe) // 2
            lemming_distance = dist_to_left if dist_to_right < dist_to_left else dist_to_right
        if lemming_distance > max_distance:
            max_distance = lemming_distance
    return max_distance
    # def furthest_best(num_holes, cafes):
    # """Find longest distance between a hole and a cafe.

    # This solution looks at the cafes, finding the two that are furthest
    # apart, and then determining which lemming hole would have to travel
    # the furthest between them.
    # """

    # # Start with the distance from first hole to the first cafe, and from
    # # the last hole to the last cafe:

    # distances = [cafes[0],
    #              num_holes - cafes[-1] - 1]

    # for i in range(1, len(cafes)):
    #     # between cafes: distance is half the distance to leftward cafe
    #     distances.append((cafes[i] - cafes[i - 1]) // 2)

    # return max(distances)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
