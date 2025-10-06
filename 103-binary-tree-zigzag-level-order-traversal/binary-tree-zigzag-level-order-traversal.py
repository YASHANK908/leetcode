from collections import deque 
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q=deque([root])
        res=[]
        left_to_right=True
        while q:
            level_size=len(q)
            level_nodes=deque()
            for _ in range(level_size):
                node=q.popleft()
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(level_nodes)) 
            left_to_right= not left_to_right
        return res               
            



        