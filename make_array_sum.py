from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        total_nums1 = sum(nums1)
        if total_nums1 <= x:
            return 0

        total_increment = sum(nums2)
        n = len(nums1)

        # Ordena nums1 e nums2 com base em nums2 para otimizar as escolhas
        nums2, nums1 = zip(*sorted(zip(nums2, nums1)))

        dp_previous = [0] * (n + 1)
        dp_current = [0] * (n + 1)

        for t in range(1, n + 1):
            for j in range(n):
                dp_current[j + 1] = max(
                    dp_current[j],
                    dp_previous[j] + nums1[j] + nums2[j] * t
                )
            total_nums1 += total_increment
            if total_nums1 - dp_current[-1] <= x:
                return t
            dp_previous, dp_current = dp_current, dp_previous
        return -1
