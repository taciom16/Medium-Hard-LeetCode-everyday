from heapq import heappush, heappop
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        MOD = 10**9 + 7

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            d, u = heappop(heap)
            if d > dist[u]:
                continue

            for v, t in adj[u]:
                new_dist = dist[u] + t
                if dist[v] > new_dist:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heappush(heap, (dist[v], v))
                elif dist[v] == new_dist:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD
