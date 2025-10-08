# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        maxindex,count=0,0
        def dfs(node,index):
            nonlocal count,maxindex
            if not node:
                return
            count+=1
            maxindex=max(maxindex,index)
            dfs(node.left,2*index)
            dfs(node.right,2*index+1)
        dfs(root,1)
        return count==maxindex            

        