from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        queue = []
        queue.append(source)
        visited[source] = True
        start_index = 0

        while start_index < len(queue):
            current = queue[start_index]
            start_index += 1
            if current == destination:
                return True
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False
