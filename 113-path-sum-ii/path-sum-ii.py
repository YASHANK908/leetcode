 
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,path,remaining):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val==remaining:
                res.append(list(path))
            else:
                dfs(node.left,path,remaining-node.val)
                dfs(node.right,path,remaining-node.val)
            path.pop()    
        dfs(root,[],targetSum)      
        return res          
        