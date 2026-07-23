# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            numLeft = dfs(node.left)
            numRight = dfs(node.right)
            
            if numLeft == -1 or numRight == -1:
                return -1
            
            if abs(numLeft - numRight) > 1:
                return -1

            return 1 + max(numLeft, numRight)
        return dfs(root) != -1

        # Time: O(n)
        # Space: O(h)

        # def dfs(node):
        #     if not node:
        #         return True
            
        #     numLeft = findHeight(node.left)
        #     numRight = findHeight(node.right)
        #     return abs(numLeft - numRight) <= 1 and dfs(node.left) and dfs(node.right)

        # def findHeight(node):
        #     if not node:
        #         return 0
        #     return 1 + max(findHeight(node.left), findHeight(node.right))

        # return dfs(root)

        # Time: O(n^2)
        # Space: O(h)
         