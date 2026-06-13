class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                box = (r // 3, c // 3)
                if board[r][c] in boxes[box]:
                    return False
                boxes[box].add(board[r][c])
        return True

        # Time: O(n^2)
        # Space: O(n^2)