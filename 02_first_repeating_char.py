"""
Find the first repeating character within the given string.
"""


def find_first_repeating_char(input_str: str) -> str:
    """
        Example:
        input_str = 'bool'
        mapper = {
            b: b
            o: o
            l: l
        }
        So the char which is repeated first is 'o'.

        Solution:
         - Time complexity: O(n)
         - Space complexity: O(n)

        :param input_str: Input string
        :returns First repeated string or end of the string char
        :rtype str
        """
    mapper = {}
    for char in input_str:
        if mapper.get(char):
            return char
        mapper[char] = char

    return '\0'


input_str1 = 'terrain!'
input_str2 = 'whiskey'
input_str3 = 'sometimes'

print(find_first_repeating_char(input_str1))
print(find_first_repeating_char(input_str2))
print(find_first_repeating_char(input_str3))
