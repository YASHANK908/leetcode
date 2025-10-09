

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[(root,root.val)]
        Sum=0

        while stack:
            node,current=stack.pop()

            if not node.left and not node.right:
                Sum+=current

            if node.right:
                stack.append((node.right,(current<<1)|node.right.val))
            if node.left:
                stack.append((node.left,(current<<1)|node.left.val))      
        return Sum              
        