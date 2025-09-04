class Solution(object):
    def findClosest(self, x, y, z):
        xz = abs(x - z)
        yz = abs(y - z)

        if xz == yz:
            return 0
        elif xz < yz:
            return 1
        else:
            return 2

        