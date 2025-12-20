class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dp=[[-math.inf] * 3 for _ in range(4)]
        dp[0][0]=0
        for x in nums:
            s=x%3
            for i in range(3,0,-1):
                for prev in range(3):
                    if dp[i-1][prev]==-math.inf:
                        continue
                    nr=(prev+s)%3
                    dp[i][nr]=max(dp[i][nr],dp[i-1][prev]+x)

        res=dp[3][0]
        return 0 if res==-math.inf else res
        
