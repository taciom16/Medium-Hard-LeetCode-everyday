from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_ones = [0] * (n + 1)
        prefix_twos = [0] * (n + 1)
        prefix_threes = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_ones[i] = prefix_ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
            prefix_twos[i] = prefix_twos[i - 1] + (1 if nums[i - 1] == 2 else 0)
            prefix_threes[i] = prefix_threes[i - 1] + (1 if nums[i - 1] == 3 else 0)

        min_removals = n

        for i in range(n + 1):
            for j in range(i, n + 1):
                kept_ones = prefix_ones[i]

                kept_twos = prefix_twos[j] - prefix_twos[i]

                kept_threes = prefix_threes[n] - prefix_threes[j]

                total_kept = kept_ones + kept_twos + kept_threes

                total_removals = n - total_kept

                if total_removals < min_removals:
                    min_removals = total_removals

        return min_removals
