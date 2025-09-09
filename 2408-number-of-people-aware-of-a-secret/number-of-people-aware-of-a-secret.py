class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(1, n + 1):
            for share_day in range(day + delay, min(day + forget, n + 1)):
                dp[share_day] = (dp[share_day] + dp[day]) % MOD

        return sum(dp[max(1, n - forget + 1): n + 1]) % MOD
