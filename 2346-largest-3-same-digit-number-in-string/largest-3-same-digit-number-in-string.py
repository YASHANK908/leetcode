class Solution(object):
    def largestGoodInteger(self, num):
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                triple = num[i:i+3]
                if triple > max_good:
                    max_good = triple
        return max_good
        