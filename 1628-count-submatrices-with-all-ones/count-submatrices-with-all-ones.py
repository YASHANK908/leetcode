class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        height = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            
            stack = []
            sum_contrib = [0] * n   
            for j in range(n):
                
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()
                
                if stack:
                    prev_index = stack[-1]
                    sum_contrib[j] = sum_contrib[prev_index] + height[j] * (j - prev_index)
                else:
                    sum_contrib[j] = height[j] * (j + 1)
                
                stack.append(j)
                res += sum_contrib[j]
        
        return res
       
        