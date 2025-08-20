class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack=[]
        maxarea=0
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                maxarea=max(maxarea,height*width)
            stack.append(i)    
        return maxarea