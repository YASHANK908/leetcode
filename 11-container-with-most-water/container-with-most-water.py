class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        maxwater=0
        while left<right:
            h=min(height[left],height[right])
            area=h*(right-left)
            maxwater=max(area,maxwater)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxwater            
         
        