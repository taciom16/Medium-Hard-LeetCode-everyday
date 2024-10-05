class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def total_apples(n):
            return 4 * n ** 3 + 6 * n ** 2 + 2 * n

        low, high = 0, 1
        while total_apples(high) < neededApples:
            high *= 2

        while low < high:
            mid = (low + high) // 2
            if total_apples(mid) >= neededApples:
                high = mid
            else:
                low = mid + 1

        perimeter = 8 * low
        return perimeter
