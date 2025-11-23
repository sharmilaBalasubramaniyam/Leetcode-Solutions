class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        m = sum(nums)                                               
        ns = m%3
        if ns == 0: return m
        
        t = [0]+ sorted(filter(lambda x:x%3 != 0, nums))[:4]    

        return m - min(map(sum,filter                               
            (lambda x: (x[0]+x[1])%3 == ns, combinations(t,2))))
