"""
Problem #73:

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""
from copy import deepcopy
from datetime import datetime

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
    [[9, 9, 9, 9, 9], [9, 0, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 0, 9], [9, 9, 9, 9, 9]],  # Test data
    [[9, 0, 9, 0, 9], [0, 0, 0, 0, 0], [9, 0, 9, 0, 9], [0, 0, 0, 0, 0], [9, 0, 9, 0, 9]]  # Expected result
)
# ... and one more test case...
test_case_4 = (
    [[1, 0, 1], [1, 0, 1], [1, 1, 1]],  # Test data
    [[0, 0, 0], [0, 0, 0], [1, 0, 1]]  # Expected result
)

tests = [
    test_case_1,
    test_case_2,
    test_case_3,
    test_case_4
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
    # Fill the 1st row, if needed
    for item in matrix:
        if item[0] != 0:
            for column in columns:
                item[column] = 0


def set_zeroes_improved(matrix: list[list[int]]) -> None:
    """
    'Improved' solution: Storing columns to be filled with 0s in the row 0
    """
    # First, we go through all the rows...
    # ... also set the flag so we know whether row 0 should be filled with 0s
    fill_first = 0 in matrix[0]
    for i in range(1, len(matrix)):
        # Iterate through the row...
        fill = 0 in matrix[i]  # Do we have to fill this row with 0s?
        for j in range(len(matrix[i])):
            # ... appending columns with zeroes to the list - only once...
            if matrix[i][j] == 0:
                matrix[0][j] = 0
            # ... and zeroing out the row, if needed
            if fill:
                matrix[i][j] = 0
    # Set 0s where they should be                
    for row in matrix:
        if 0 not in row:
            for i in range(len(row)):
                if matrix[0][i] == 0:
                    row[i] = 0
    # Fill the 1st row, if needed
    if fill_first:
        matrix[0] = [0 for _ in range(len(matrix[1]))]


if __name__ == '__main__':

    for test, expected in tests:
        actual_1 = deepcopy(test)
        actual_2 = deepcopy(test)
        start_time_1 = datetime.now()
        set_zeroes_brute(actual_1)
        brute_force_time = datetime.now() - start_time_1

        start_time_2 = datetime.now()
        set_zeroes_improved(actual_2)
        improved_time = datetime.now() - start_time_2

        print(f"Brute force function - started at {start_time_1}")
        print(f"Improved function - started at {start_time_2}")
        print(f"Test data:\n{test}")
        print(f"Bruteforce test result: {'Passed' if actual_1 == expected else 'Failed'}")
        print(f"Improved test result: {'Passed' if actual_2 == expected else 'Failed'}")
        print(f"Expected:          {expected}")
        print(f"Actual bruteforce: {actual_1}")
        print(f"Actual improved:   {actual_2}")
        print(f"Execution time - bruteforce: {brute_force_time}")
        print(f"Execution time - improved:   {improved_time}")
        if brute_force_time > improved_time:
            longer = "Bruteforce"
            diff = brute_force_time - improved_time
        elif brute_force_time < improved_time:
            longer = "Improved"
            diff = improved_time - brute_force_time
        else:
            longer = "None"
            diff = "0 (or negligible)"
        print(f"{longer} is longer by {diff} seconds")
