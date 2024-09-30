class Solution:
    def climbStairs(self, number: int) -> int:
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2

        first = 1
        second = 2
        for _ in range(3, number + 1):
            current = first + second
            first, second = second, current

        return second
