 
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff=0

        def dfs(node,curr_min,curr_max):
            if not node:
                return
            self.max_diff=max(self.max_diff,abs(node.val-curr_min),abs(node.val-curr_max))
            curr_min=min(curr_min,node.val)
            curr_max=max(curr_max,node.val)

            dfs(node.left,curr_min,curr_max)
            dfs(node.right,curr_min,curr_max)
        dfs(root,root.val,root.val)    
        return self.max_diff        
        