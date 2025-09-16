try:
    from math import gcd  
except ImportError:
    from fractions import gcd  

class Solution(object):
    def replaceNonCoprimes(self, nums):
        stack = []
        
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                prev = stack.pop()
                num = (prev * num) // gcd(prev, num)
            stack.append(num)
        
        return stack
