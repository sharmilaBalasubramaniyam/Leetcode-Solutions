class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        i=n-1

        while i>=0 and nums[i] not in seen:
            seen.add(nums[i])
            i-=1

        if i<0:
            return 0

        return (i+1+2)//3
