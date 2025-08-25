class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize row with all 1s
            for j in range(1, i):  # Fill middle values
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res
         
        