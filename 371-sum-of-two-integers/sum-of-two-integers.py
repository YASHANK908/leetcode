class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=0xFFFFFFFF
        MAX_INT=0X7FFFFFFF
        while b!=0:
            partial_sum=(a^b)&MASK
            carry=((a&b)<<1)&MASK
            a,b=partial_sum,carry
        return a if a<=MAX_INT else ~(a^MASK)
        