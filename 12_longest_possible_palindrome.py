"""
Longest possible palindrome.

Solution:
 - Time complexity: O(n)
 - Space complexity: O(1)
"""


def longest_palindrome(string):
    occurrences = [0] * 128
    for letter in string:
        occurrences[ord(letter)] += 1
    length = 0
    for occurrence in occurrences:
        length += occurrence if occurrence % 2 == 0 else occurrence - 1
    if length < len(string):
        length += 1
    return length


test_str = 'abccccdd'
print(longest_palindrome(test_str))
