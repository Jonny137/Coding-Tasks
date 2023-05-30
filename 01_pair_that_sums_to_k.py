"""
Find a pair of elements within the given array
which sum to a defined integer k.
"""


def check_pair_sum_to_k(arr: list, k: int) -> bool:
    """
    Example:
    arr = [3, 5, 7, 10]
    k = 10
    mapper = {
        3: 7
        5: 5
        7: 3
        10: 0
    }
    So the values which form 10 would be 3 and 7 -> True

    Solution:
     - Time complexity: O(n)
     - Space complexity: O(n)

    :param arr: Input array
    :param k: Defined integer sum
    :returns Bool value which tells us whether the array holds two elements
             that sum to k or not
    :rtype bool
    """
    mapper = {}

    for element in arr:
        diff = k - element
        if mapper.get(diff):
            return True
        mapper[element] = diff

    return False


arr1 = [3, 5, 2, 10]
k1 = 10
arr2 = [2, 12, 21, 11]
k2 = 7
arr3 = [5, 5, 7, 3]
k3 = 10
arr4 = [1, 5, 2, 9]
k4 = 10

print(check_pair_sum_to_k(arr1, k1))
print(check_pair_sum_to_k(arr2, k2))
print(check_pair_sum_to_k(arr3, k3))
print(check_pair_sum_to_k(arr4, k4))
