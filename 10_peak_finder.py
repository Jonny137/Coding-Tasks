"""
Peak finder.

Solution:
 - Time complexity: O(logn)
 - Space complexity: O(1)
"""


def find_peak_recursively(arr, left, right):
    if left >= right:
        return left
    mid = (left + right)//2
    if arr[mid] < arr[mid+1]:
        return find_peak_recursively(arr, mid+1, right)
    else:
        return find_peak_recursively(arr, left, mid)


def find_peak(arr):
    return find_peak_recursively(arr, 0, len(arr)-1)


array = [2, 5, 15, 23, 12, 44, 1]
print(find_peak(array))
