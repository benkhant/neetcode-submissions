# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # optimized solution using dfs

        stack = []
        node = root
        count = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if k == count: 
                return node.val
            node = node.right
        
        # brute force
        # if not root:
        #     return []
        # res = []
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     res.append(node.val)
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)

        # res.sort()

        # return res[k - 1]