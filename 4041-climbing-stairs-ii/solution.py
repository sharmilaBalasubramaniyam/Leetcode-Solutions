class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        ans = costs
        dp = [0] + [10**18] * n

        for j in range(1, n + 1):
            for step in(1,2,3):
                if j - step >= 0:
                    dp[j] = min(dp[j], dp[j - step] + ans[j - 1] + (step ** 2))

        return dp[n]
