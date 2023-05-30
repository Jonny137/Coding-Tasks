"""
Jump to last index.
By keeping track of the max index that we can reach

Solution:
 - Time complexity: O(n)
 - Space complexity: O(1)
"""


def can_jump(arr):
    n = len(arr)
    max_index = 0
    for i in range(n):
        if i > max_index:
            return False
        else:
            max_index = max(max_index, i + arr[i])
    return max_index >= n - 1


test_array_1 = [5, 3, 2, 0, 1, 0, 4]
test_array_2 = [3, 0, 2, 0, 2, 1, 4, 3]
print(can_jump(test_array_1))
print(can_jump(test_array_2))
