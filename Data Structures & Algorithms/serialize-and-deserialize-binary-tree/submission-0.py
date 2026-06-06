# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root: 
            return ""

        q = deque([root])
        while q: 
            node = q.popleft()
            if node is None: 
                res.append("null")
                continue

            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        res = data.split(",")
        if not res or res[0] == "null":
            return None

        root = TreeNode(int(res[0]))
        q = deque([root])
        i = 1
        
        while q and i < len(res):
            node = q.popleft()

            # left subtree
            if i < len(res):
                tok = res[i];
                i += 1
                if tok and tok != "null":
                    node.left = TreeNode(int(tok))
                    q.append(node.left)

            # right subtree
            if i < len(res):
                tok = res[i];
                i += 1
                if tok and tok != "null":
                    node.right = TreeNode(int(tok))
                    q.append(node.right)

        return root
