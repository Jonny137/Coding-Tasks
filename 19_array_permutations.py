"""
Flatten binary tree.

Solution:
 - Time complexity: O(n*n!)
 - Space complexity: O(n*n!)
"""


def get_next_greater_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return arr
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[:i:-1]
    return arr


def get_permutations(arr):
    if len(arr) < 2:
        return [arr]
    arr = sorted(arr)
    permutations = [arr.copy()]
    greatest_permutation = arr[::-1]
    while arr != greatest_permutation:
        arr = get_next_greater_permutation(arr)
        permutations.append(arr.copy())
    return permutations


arr1 = [3, 5, 2, 10]
print(get_permutations(arr1))
