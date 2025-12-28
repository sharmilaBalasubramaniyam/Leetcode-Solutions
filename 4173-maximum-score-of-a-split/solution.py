class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n=len(nums)

        ps=[0]*n
        ps[0]=nums[0]
        for i in range(1,n):
            ps[i]=ps[i-1]+nums[i]

        sm=[0]*n
        sm[n-1]=float('inf')
        cm=float('inf')
        for i in range(n-2,-1,-1):
            cm=min(cm,nums[i+1])
            sm[i]=cm

        res=float('-inf')
        for i in range(n-1):
            res=max(res,ps[i]-sm[i])
        return res
    
        
        
