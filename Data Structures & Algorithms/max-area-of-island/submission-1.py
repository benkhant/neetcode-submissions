class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            return 1 + sum(dfs(r + dr, c + dc) for dr, dc in directions)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea,  dfs(r, c))
        return maxArea

        # Time: O(m*n)
        # Space: O(m*n)