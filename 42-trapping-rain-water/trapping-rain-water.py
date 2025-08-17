class Solution(object):
    def trap(self, height):
        left,right=0,len(height)-1
        maxleft=maxright=0
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=maxleft:
                    maxleft=height[left]
                else:
                    water+=maxleft-height[left]
                left+=1    
            else:
                if height[right]>=maxright:
                    maxright=height[right]
                else:
                    water+=maxright-height[right]
                right-=1    
        return water                        
        