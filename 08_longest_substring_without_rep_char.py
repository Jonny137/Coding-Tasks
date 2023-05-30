"""
Find a longest substring withing a string without repeating characters.

Solution:
 - Time complexity: O(n)
 - Space complexity: O(1)
"""


def longest_substring_without_repeating_characters(string):
    max_length = 0
    start = 0
    indexes = [-1] * 128
    for i in range(len(string)):
        if indexes[ord(string[i])] >= start:
            start = indexes[ord(string[i])]+1
        indexes[ord(string[i])] = i
        max_length = max(max_length, i-start+1)
    return max_length


test1 = 'somerandomstringwithoutrepeatingchars'
print(longest_substring_without_repeating_characters(test1))
