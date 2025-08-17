class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        maxarea=0
        while left<right:
            width=right-left
            currentarea=min(height[left],height[right])*width
            maxarea=max(maxarea,currentarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea            

        