class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n=len(s)
        res=float('inf')
        for t in set(s):
            crr=0
            for ch,c in zip(s,cost):
                if ch!=t:
                    crr+=c
            res=min(res,crr)
        return res
        
