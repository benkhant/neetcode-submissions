class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevVal):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if (r, c) in visited:
                return
            if heights[r][c] < prevVal:
                return 
            visited.add((r, c))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols-1])
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows-1][c])

        return [[r, c] for r in range(rows) for c in range(cols)
                if (r, c) in pac and (r, c) in atl]

        # Time: O(m*n)
        # Space: O(m*n)