# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(tree, subTree):
            if not tree and not subTree:
                return True
            if not tree or not subTree:
                return False
            if tree.val != subTree.val:
                return False
            return isSametree(tree.left, subTree.left) and isSametree(tree.right, subTree.right)

        if not root:
            return False

        if isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # Time: O(n*m)
        # Space: O(h)