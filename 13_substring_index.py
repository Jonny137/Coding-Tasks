"""
Get substring index.
(Knuth-Morris-Pratt algorithm)

Solution:
 - Time complexity: O(n)
 - Space complexity: O(m)
"""


def get_longest_possible_array(string):
    longest_possible_array = [0] * len(string)
    length = 0
    i = 1
    while i < len(string):
        if string[i] == string[length]:
            length += 1
            longest_possible_array[i] = length
            i += 1
        elif length > 0:
            length = longest_possible_array[length-1]
        else:
            longest_possible_array[i] = 0
            i += 1
    return longest_possible_array


def substring_index(string1, string2):
    n = len(string1)
    m = len(string2)
    if m > n:
        return -1
    if m == n:
        return 0 if string2 == string1 else -1
    if string2 == "":
        return 0
    longest_possible_array = get_longest_possible_array(string2)
    j = 0
    i = 0
    while i < n and j < m:
        if string1[i] == string2[j]:
            i += 1
            j += 1
        elif j > 0:
            j = longest_possible_array[j-1]
        else:
            i += 1
    return -1 if j < m else i-j


test_string = 'Something funny within the forest.'
test_sub = 'funny'

print(substring_index(test_string, test_sub))  # should return 10
