# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def dfs(node):

            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            diam = leftHeight + rightHeight
            self.maxDiam = max(self.maxDiam, diam)

            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return self.maxDiam

        # Time: O(n)
        # Space: O(h)

        # self.maxDiam = 0

        # def dfs(node):
        #     if not node:
        #         return 0

        #     diam = maxHeight(node.left) + maxHeight(node.right)
        #     self.maxDiam = max(self.maxDiam, diam)

        #     dfs(node.left)
        #     dfs(node.right)
    
        # def maxHeight(node):
        #     if not node:
        #         return 0

        #     return 1 + max(maxHeight(node.left), maxHeight(node.right))
        
        # dfs(root)

        # return self.maxDiam

        # Time: O(n^2)
        # Space: O(h)