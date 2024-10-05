from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(1 << 25)

        n = len(parents)
        tree = [[] for _ in range(n)]
        root = -1

        for child, parent in enumerate(parents):
            if parent == -1:
                root = child
            else:
                tree[parent].append(child)

        from collections import defaultdict
        node_queries = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            node_queries[node].append((val, idx))

        ans = [0] * len(queries)

        MAX_BIT = 18
        root_trie = TrieNode()

        def insert(num):
            node = root_trie
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1

        def remove(num):
            node = root_trie
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                child = node.children[bit]
                child.count -= 1
                if child.count == 0:
                    node.children[bit] = None
                    return
                node = child

        def max_xor(val):
            node = root_trie
            res = 0
            for i in range(MAX_BIT, -1, -1):
                bit = (val >> i) & 1
                toggled_bit = 1 - bit
                if node.children[toggled_bit]:
                    res |= (1 << i)
                    node = node.children[toggled_bit]
                elif node.children[bit]:
                    node = node.children[bit]
                else:
                    break
            return res

        def dfs(u):
            insert(u)
            for val, idx in node_queries[u]:
                ans[idx] = max_xor(val)
            for v in tree[u]:
                dfs(v)
            remove(u)

        dfs(root)
        return ans
