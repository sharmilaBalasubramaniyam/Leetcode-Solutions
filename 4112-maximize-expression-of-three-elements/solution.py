class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n=len(nums)
        mv=float('-inf')
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if len({i,j,k}) == 3:
                        mv=max(mv,nums[i]+nums[j]-nums[k])
        return mv
        
