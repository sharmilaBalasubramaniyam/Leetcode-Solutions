class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def on(k):
            s=0
            for x in nums:
                s+=(x+k-1)//k
            return s
        l,r=1,sum(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            if on(mid)<=mid*mid:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
