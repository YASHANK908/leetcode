 
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        total=0
        for node in reversed(nodes):
            total+=node.val
            node.val=total
        return root  
        