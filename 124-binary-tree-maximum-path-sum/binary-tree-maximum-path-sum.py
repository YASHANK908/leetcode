# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')
        def maxgain(node):
            if not node:
                return 0
            left_gain=max(maxgain(node.left),0)
            right_gain=max(maxgain(node.right),0)

            self.maxsum=max(self.maxsum,node.val+left_gain+right_gain)
            return node.val+max(left_gain,right_gain)
        maxgain(root)
        return self.maxsum