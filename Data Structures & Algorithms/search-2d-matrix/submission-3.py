class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False

        # Time: O(log(m * n))
        # Space: O(1)

        # rows = len(matrix)
        # cols = len(matrix[0])

        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == target:
        #             return True
        # return False

        # Time: O(m*n)
        # Space: O(1)