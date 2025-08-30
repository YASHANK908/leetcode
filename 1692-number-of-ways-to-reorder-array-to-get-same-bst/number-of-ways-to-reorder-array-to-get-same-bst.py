MOD = 10**9 + 7

class Solution(object):
    def __init__(self):
        self.fact = []
        self.invFact = []

    def precompute_factorials(self, n):
        self.fact = [1] * (n+1)
        self.invFact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1] * i % MOD
        self.invFact[n] = pow(self.fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            self.invFact[i-1] = self.invFact[i] * i % MOD

    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.invFact[r] % MOD * self.invFact[n-r] % MOD

    def helper(self, nums):
        if len(nums) <= 2:
            return 1
        root = nums[0]
        left = [x for x in nums if x < root]
        right = [x for x in nums if x > root]
        leftWays = self.helper(left)
        rightWays = self.helper(right)
        return self.nCr(len(left)+len(right), len(left)) * leftWays % MOD * rightWays % MOD

    def numOfWays(self, nums):
        self.precompute_factorials(len(nums))
        return (self.helper(nums) - 1) % MOD