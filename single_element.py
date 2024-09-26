#O enunciado O(log n) deixou muito na cara que era uma busca bina'ria, aí ficou chato.
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2

            if mid_index % 2 == 1:
                mid_index -= 1

            if nums[mid_index] == nums[mid_index + 1]:
                left = mid_index + 2
            else:
                right = mid_index

        return nums[left]
