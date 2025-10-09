from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum+=node.val
            count=prefix_count[current_sum-targetSum]

            prefix_count[current_sum]+=1
            count+=dfs(node.left,current_sum)
            count+=dfs(node.right,current_sum)

            prefix_count[current_sum]-=1

            return count
        return dfs(root,0)        
        