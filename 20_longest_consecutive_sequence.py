"""
Longest consecutive sequence.
Optimized brute force

Solution:
 - Time complexity: O(n)
 - Space complexity: O(n)
"""


def longest_consecutive_sequence(arr):
    if len(arr) < 2:
        return len(arr)
    max_length = 1
    values = set(arr)
    for element in values:
        if element - 1 in values:
            continue
        else:
            right = element
            while right + 1 in values:
                right += 1
            max_length = max(max_length, right - element + 1)
    return max_length


arr1 = [14, 1, 8, 4, 0, 13, 6, 9, 2, 7]
print(longest_consecutive_sequence(arr1))
