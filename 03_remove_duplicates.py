"""
Remove the duplicated elements from the given array of integers.
"""


def remove_duplicates(arr: list) -> list:
    """
    Method which should remove duplicated elements within array

    Example:
    arr = [1, 3, 5, 3, 7]

    Solution:
     - Time complexity: O(n)
     - Space complexity: O(n)

    Exploit the unique key constrain in python dicts and return it's keys
    (alternative work with sets e.g. -> return set(input_arr))

    :param arr: Input array with possible duplicates
    :return: Input array without duplicates
    :rtype: list
    """
    mapper = {}
    for element in arr:
        mapper[element] = element

    return list(mapper.keys())


input_arr1 = [1, 3, 5, 3, 7]
input_arr2 = [1, 3, 5, 7]
input_arr3 = [1, 3, 5, 3, 7, 7, 3, 6, 2, 2, 12]
print(remove_duplicates(input_arr1))
print(remove_duplicates(input_arr2))
print(remove_duplicates(input_arr3))
