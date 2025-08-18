 
class Solution(object):
    def judgePoint24(self, cards):
        target = 24.0
        TOL = 1e-6

        # Convert all numbers to floats to avoid integer division issues (works on Py2 & Py3)
        nums = [float(x) for x in cards]

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - target) < TOL

            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = nums[i], nums[j]
                    # remove by index (safe even with duplicates because we're using indices)
                    rest = [nums[k] for k in range(n) if k != i and k != j]

                    # all possible results from combining a and b
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > 1e-9:
                        candidates.append(a / b)
                    if abs(a) > 1e-9:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs(nums)