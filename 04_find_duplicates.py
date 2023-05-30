"""
Find the duplicated element within the array of integers size n + 1, where
element values can range from 1 to n.
Constraints:
 - The array can hold only one duplicated element
 - Duplicated element can appear more then once within the array

"""


def find_duplicates(arr: list) -> int:
    """
    Optimal would be to use Floyd's Cycle Detection algorithm.
    (Tortoise and Hare)

    Solution:
     - Time complexity: O(n)
     - Space complexity: O(1)

    :param arr: Input array
    :return: Duplicated element
    :rtype: int
    """
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise


input_list1 = [1, 3, 5, 4, 1]
input_list2 = [2, 0, 4, 4, 4, 1]
input_list3 = [1, 2, 3, 4, 3, 3]

print(find_duplicates(input_list1))
print(find_duplicates(input_list2))
print(find_duplicates(input_list3))
