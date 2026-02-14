class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n=len(nums)

        if n==0:
            return 0
        if n==1:
            return nums[0]

        dp=[0]*n
        dp[0]=nums[0]

        if colors[0]==colors[1]:
            dp[1]=max(nums[0],nums[1])
        else:
            dp[1]=nums[0]+nums[1]

        for i in range(2,n):
            if colors[i]==colors[i-1]:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            else:
                dp[i]=dp[i-1]+nums[i]
        return dp[n-1]
        
