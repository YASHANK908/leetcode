# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res,stack=[],[]
        lastvisited=None
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            peek=stack[-1]
            if peek.right and peek.right!=lastvisited:
                curr=peek.right
            else:
                res.append(peek.val)
                lastvisited=stack.pop()        
        return res