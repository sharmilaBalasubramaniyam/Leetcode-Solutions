class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #    seen={}

        #    for i,num in enumerate(nums):

        #        c=target-num

        #        if c in seen:
        #            return [seen[c],i]
                
        #        seen[num]=i

        #n=len(nums)

        #for i in range(n):
        #    for j in range(i+1,n):
        #        if nums[i]+nums[j]==target:
        #           return [i,j]
                    
        seen={}

        for i,num in enumerate(nums):
            c=target-num

            if c in seen:
                return [seen[c],i]
            seen[num]=i
        
            
        
