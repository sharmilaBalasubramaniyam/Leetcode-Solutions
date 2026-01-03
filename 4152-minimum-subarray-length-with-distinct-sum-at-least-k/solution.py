from collections import defaultdict
from typing import List
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        freq=defaultdict(int)
        ds=0
        res=float('inf')

        for r,x in enumerate(nums):
            if freq[x]==0:
                ds+=x
            freq[x]+=1

            while l<=r and ds>=k:
                res=min(res,r-l+1)
                y=nums[l]
                freq[y]-=1
                if freq[y]==0:
                    ds-=y
                l+=1
        return res if res!=float('inf') else -1
        
        
