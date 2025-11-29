class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]       
        rs = s[::-1]          

        flips = 0
        for i in range(len(s)):
            if s[i] != rs[i]:
                flips += 1

        return flips