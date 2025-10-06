from collections import deque 
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res=[]  
        q=deque([root])  

        while q:
            level_size=len(q)
            level_nodes=[]
            for _ in range(level_size):
                node=q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_nodes)
        return res                
        