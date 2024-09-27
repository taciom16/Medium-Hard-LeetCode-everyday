from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        nums_length = len(nums)
        for current_index in range(nums_length):
            if current_index > 0 and nums[current_index] == nums[current_index - 1]:
                continue
            left_index = current_index + 1
            right_index = nums_length - 1
            while left_index < right_index:
                total = nums[current_index] + nums[left_index] + nums[right_index]
                if total < 0:
                    left_index += 1
                elif total > 0:
                    right_index -= 1
                else:
                    result.append([nums[current_index], nums[left_index], nums[right_index]])
                    while left_index < right_index and nums[left_index] == nums[left_index + 1]:
                        left_index += 1
                    while left_index < right_index and nums[right_index] == nums[right_index - 1]:
                        right_index -= 1
                    left_index += 1
                    right_index -= 1
        return result
