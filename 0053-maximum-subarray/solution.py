class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        currsum=maxsum=nums[0]

        for i in range(1,len(nums)):
            currsum=max(nums[i],currsum+nums[i])
            maxsum=max(maxsum,currsum)
        return maxsum
        
