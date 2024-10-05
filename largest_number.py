from typing import List


class Solution:
    def largestNumber(self, numbers: List[int]) -> str:
        number_to_string = [str(number) for number in numbers]

        max_len = max(len(s) for s in number_to_string)

        def sort_key(s):
            extended = s * (max_len * 2)
            return extended[:max_len * 2]

        number_to_string.sort(key = sort_key, reverse =True)

        if number_to_string[0] == '0':
            return '0'

        return ''.join(number_to_string)
