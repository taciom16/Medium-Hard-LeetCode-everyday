from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_subarray_length = float('inf')
        or_to_length = {}

        for num in nums:
            next_or_to_length = {}

            new_or = num
            new_length = 1

            if new_or >= k:
                min_subarray_length = min(min_subarray_length, new_length)
            next_or_to_length[new_or] = new_length

            for prev_or, prev_length in or_to_length.items():
                combined_or = prev_or | num
                combined_length = prev_length + 1

                if combined_or >= k:
                    min_subarray_length = min(min_subarray_length, combined_length)

                if (combined_or not in next_or_to_length or
                    next_or_to_length[combined_or] > combined_length):
                    next_or_to_length[combined_or] = combined_length

            or_to_length = next_or_to_length
        return min_subarray_length if min_subarray_length != float('inf') else -1
