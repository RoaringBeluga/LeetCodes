"""
Problem #73:

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""

# Simplest test case...
test_case_1 = (
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],  # Test data
    [[1, 0, 1], [0, 0, 0], [1, 0, 1]]  # Expected result
)
# ... and a more complicated one ...
test_case_2 = (
    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],  # Test data
    [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]  # Expected result
)
# ... and more complicated again
test_case_3 = (
    [[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 91]],  # Test data
    [[1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 91]]  # Expected result
)

tests = [
    test_case_1,
    test_case_2,
    test_case_3
]


def set_zeroes_brute(matrix: list[list[int]]) -> None:
    """
    Brute force solution
    """
    columns = []  # List of columns to be zeroed out
    # First, we go through all the rows...
    for index, item in enumerate(matrix):
        # Now if we have at least one zero in the row...
        if 0 in item:
            # ... we iterate through the row...
            for idx, element in enumerate(item):
                # ... appending columns with zeroes to the list - only once...
                if element == 0 and idx not in columns:
                    columns.append(idx)
                # ... and zeroing out the row
                item[idx] = 0
    for item in matrix:
        if item[0] != 0:
            for column in columns:
                item[column] = 0


if __name__ == '__main__':
    for test, expected in tests:
        actual = test.copy()
        set_zeroes_brute(actual)
        print(f"Test data:\n{actual}")
        print(f"Test result: {'Passed' if actual == expected else 'Failed'}")
        print(f"Expected: {expected}")
        print(f"  Actual: {actual}")
