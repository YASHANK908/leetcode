class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<2:
            return []
        left=0
        right=len(numbers)-1
        while left<right:
            Sum=numbers[left]+numbers[right]
            if Sum==target:
                return [left+1,right+1]
            elif Sum<target:
                left+=1
            else:
                right-=1
        