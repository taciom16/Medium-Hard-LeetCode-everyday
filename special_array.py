from typing import List


class Solution:
    def isArraySpecial(self, numbers: List[int]) -> bool:
        if len(numbers) == 1:
            return True

        for i in range(len(numbers) - 1):
            current = numbers[i]
            next_num = numbers[i + 1]

            current_parity = current % 2
            next_parity = next_num % 2

            if current_parity == next_parity:
                return False
        return True
