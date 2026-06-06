class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == -1):
                return

            q.append([r, c])
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dis = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft() 
                grid[r][c] = dis
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dis += 1

        # time: O(m*n)
        # space: O(m*n)
