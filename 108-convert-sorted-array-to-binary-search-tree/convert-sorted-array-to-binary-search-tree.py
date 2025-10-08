 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo,hi):
            if lo>hi:
                return None
            mid=(lo+hi)//2
            node=TreeNode(nums[mid])
            node.left=build(lo,mid-1)
            node.right=build(mid+1,hi)
            return node
        return build(0,len(nums)-1)        
        