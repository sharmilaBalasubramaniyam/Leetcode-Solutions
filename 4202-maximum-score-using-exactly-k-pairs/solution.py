class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n,m=len(nums1),len(nums2)

        dp=[[-10 ** 18] * (m+1) for _ in range(k+1)]
        dp[0]=[0]*(m+1)

        for i in range(1,n+1):
            for t in range(min(i,k),0,-1):
                for j in range(m):
                    dp[t][j+1]=max(dp[t][j+1],dp[t][j],dp[t-1][j]+nums1[i-1] * nums2[j])
        return max(dp[k])
