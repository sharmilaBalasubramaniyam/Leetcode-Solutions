class Solution:
    def finalElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        #if n==2:
        #    return max(nums)
        #nums.sort()
        return max(nums[0],nums[-1])
        
