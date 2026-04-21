class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        n=len(heights)

        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                top=stack.pop()
                h=heights[top]

                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                maxarea=max(maxarea,h*width)
            stack.append(i)


        while stack:
            top=stack.pop()
            h=heights[top]

            if not stack:
                width=n
            else:
                width=n-stack[-1]-1
            maxarea=max(maxarea,h*width)
        return maxarea        
        