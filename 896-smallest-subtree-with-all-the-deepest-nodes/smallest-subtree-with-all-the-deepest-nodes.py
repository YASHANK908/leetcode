# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0,None
            leftdepth,left=dfs(node.left)
            rightdepth,right=dfs(node.right)
            if leftdepth>rightdepth:
                return (1+leftdepth,left)
            elif rightdepth>leftdepth:
                return (1+rightdepth,right)
            return (1+leftdepth,node)
        return dfs(root)[1]
        