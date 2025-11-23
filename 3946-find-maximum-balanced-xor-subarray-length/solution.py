class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        px,ec,oc=0,0,0
        s={(0,0):-1}
        ml=0
        for i in range(n):
            px^=nums[i]
            if nums[i]%2==0:
                ec+=1
            else:
                oc+=1
            diff=ec-oc
            key=(px,diff)

            if key in s:
                ml=max(ml,i-s[key])
            else:
                s[key]=i
        return ml
        
