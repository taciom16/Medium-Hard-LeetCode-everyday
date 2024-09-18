class Solution(object):
    def maxScore(self, nums, x):
        dp_even = float('-inf')
        dp_odd = float('-inf')

        if nums[0] % 2 == 0:
            dp_even = nums[0]
        else:
            dp_odd = nums[0]

        for num in nums[1:]:
            if num % 2 == 0:
                dp_even = num + max(dp_even, dp_odd - x)
            else:
                dp_odd = num + max(dp_odd, dp_even - x)

        return max(dp_even, dp_odd)
