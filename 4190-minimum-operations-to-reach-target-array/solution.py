class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        nc=set()
        for i in range(len(nums)):
            if nums[i]!=target[i]:
                nc.add(nums[i])
        return len(nc)
        
        
