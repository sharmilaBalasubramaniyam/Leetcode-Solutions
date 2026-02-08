class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n-1):
            rs=0
            rc=0
            for j in range(i+1,n):
                rs+=nums[j]
                rc+=1
            a=rs/rc

            if nums[i]>a:
                c+=1
        return c
        
