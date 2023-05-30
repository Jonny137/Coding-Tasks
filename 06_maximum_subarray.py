"""
Given an array of integers arr, create a function that returns the sum of
the subarray that has the greatest sum. And we don't consider the empty
array as a subarray.
"""


def find_max_subarray(arr: list) -> int:
    """
    Optimal solution -> Kadane's algorithm

    Solution:
     - Time complexity: O(n)
     - Space complexity: O(1)

    :param arr: Input array
    :return: Sum of a maximum subarray
    :rtype int
    """
    global_sum = -1000000
    local_sum = 0
    for element in arr:
        local_sum = max(element, local_sum + element)
        global_sum = max(global_sum, local_sum)

    return global_sum


input_arr1 = [1, 0, 7, 10]
input_arr2 = [11, 0, -7, 12]
input_arr3 = [2, 3, -8, 4, 1]

print(find_max_subarray(input_arr1))
print(find_max_subarray(input_arr2))
print(find_max_subarray(input_arr3))
