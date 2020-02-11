# Take in a 2D matrix of 0s and 1s
# 1 is a wall, 0 is a pipe
# Water needs to flow from the top to the bottom
# Can only flow down, left, and right (no up or diagonals)


def is_valid_blueprint(blueprint):
    for column in blueprint[0]:
        if blueprint[0][column] == 0:
            return_value = recursiveWaterTravel(blueprint, (0, column))
            if return_value:
                return True
    # If no 0 on the first row, then there is no place for the water to start
    # flowing
    return False


def recursiveWaterTravel(blueprint, coords, visited=None):
    if not visited:
        visited = set()
    if coords[0] == len(blueprint) - 1:
        # Traveled to the bottom row
        return True
    visited.add(coords)
    moves = valid_moves(blueprint, coords)
    for move in moves:
        if move in visited:
            continue
        return_value = recursiveWaterTravel(blueprint, move, visited)
        if return_value:
            return True
    return False


def valid_moves(blueprint, coords):
    output_lst = []
    # Down
    if (
        coords[0] < len(blueprint) - 1
        and blueprint[coords[0] + 1][coords[1]] == 0
    ):
        output_lst.append((coords[0] + 1, coords[1]))
    # Left
    if coords[1] > 0 and blueprint[coords[0]][coords[1] - 1] == 0:
        output_lst.append((coords[0], coords[1] - 1))
    # Right
    if (
        coords[1] < len(blueprint[0]) - 1
        and blueprint[coords[0]][coords[1] + 1] == 0
    ):
        output_lst.append((coords[0], coords[1] + 1))
    return output_lst


tests = [
    ([[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0]], True),
    ([[1, 1], [1, 1]], False),
    ([[1, 1, 1], [1, 0, 1], [1, 0, 1]], False),
    ([[0, 1, 1], [1, 0, 1], [1, 0, 1]], False),
]
for num, tup in enumerate(tests):
    testcase, expected = tup
    result = is_valid_blueprint(testcase)
    success = "SUCCESS" if result == expected else "FAILURE"
    print(f"{num + 1}. {testcase} -> {expected}: {success}!")
