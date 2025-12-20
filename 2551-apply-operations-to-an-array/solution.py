class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ind=0

        for i in range(n):
            if i<n-1 and nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            
            if nums[i]!=0:
                nums[ind]=nums[i]
                ind+=1
            
        for i in range(ind,n):
            nums[i]=0
        
        return nums
    
        
