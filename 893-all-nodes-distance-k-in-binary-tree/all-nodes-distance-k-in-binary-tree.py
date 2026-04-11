# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def mark_parents(node,par=None):
            if not node:
                return
            parent[node]=par
            mark_parents(node.left,node)
            mark_parents(node.right,node)
        mark_parents(root)
        res=[]
        def dfs(node,prev,dist):
            if not node:
                return
            if dist==k:
                res.append(node.val)
                return
            for nei in (node.left,node.right,parent[node]):
                if nei!=prev:
                    dfs(nei,node,dist+1)
        dfs(target,None,0)
        return res
        
        