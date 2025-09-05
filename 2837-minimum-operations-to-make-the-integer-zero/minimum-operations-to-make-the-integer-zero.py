class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        for k in range(61):
            target = num1 - k * num2
            if target >= 0:
                # popcount: count of 1-bits in binary
                bitcount = bin(target).count("1")
                if bitcount <= k <= target:
                    return k
        return -1
        