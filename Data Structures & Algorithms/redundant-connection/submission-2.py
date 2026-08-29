class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[px] += 1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        # Time: O(n * α(n)) ≈ O(n)  ← α is inverse Ackermann function
        # Space: O(n)