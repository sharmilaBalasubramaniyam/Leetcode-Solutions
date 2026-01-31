class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        from bisect import bisect_left
        res=0
        for b in range(32):
            l=[]
            for x in nums:
                if (x>>b)&1:
                    pos=bisect_left(l,x)
                    if pos==len(l):
                        l.append(x)
                    else:
                        l[pos]=x
            res=max(res,len(l))
        return res
        
