class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        v=[]
        ind=[]
        for i,num in enumerate(nums):
            if num >= 0:
                v.append(num)
                ind.append(i)

        if len(v)<=1:
            return nums

        k%=len(v)

        rotate=v[k:]+v[:k]

        for idx,val in zip(ind,rotate):
            nums[idx]=val
        return nums
            
        
