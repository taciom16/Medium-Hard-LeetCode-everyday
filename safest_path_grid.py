from typing import List
from collections import deque

class Solution:

    def is_path_possible(self, distance, safeness_factor, n):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        visited = [[False] * n for _ in range(n)]

        if distance[0][0] < safeness_factor:
            return False

        queue.append((0, 0))
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if (r, c) == (n - 1, n - 1):
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if not visited[nr][nc] and distance[nr][nc] >= safeness_factor:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('inf')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        distance = [[-1] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    queue.append((r, c))

        #BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if distance[nr][nc] == -1:
                        distance[nr][nc] = distance[r][c] + 1
                        queue.append((nr, nc))

        max_distance = max(max(row) for row in distance)
        left, right = 0, max_distance

        result = 0

        #Busca binária
        while left <= right:
            mid = (left + right) // 2
            if self.is_path_possible(distance, mid, n):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
