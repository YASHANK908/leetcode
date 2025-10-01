class Solution(object):
    def maximalRectangle(self, matrix):
        def largestRectangleArea(heights):
            stack=[]
            heights.append(0)
            maxarea=0
            for i,h in enumerate(heights):
                while stack and h<heights[stack[-1]]:
                    height=heights[stack.pop()]
                    width=i if not stack else i-stack[-1]-1
                    maxarea=max(maxarea,width*height)
                stack.append(i)
            heights.pop()  
            return maxarea
        if not matrix:
            return 0
        maxarea=0
        cols=len(matrix[0])
        heights=[0]*cols

        for row in matrix:
            for j in range(cols):
                heights[j]=heights[j]+1 if row[j]=='1' else 0
            maxarea=max(maxarea,largestRectangleArea(heights))    
        return maxarea              

        
        
        