class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        cur=None

        for i in nums:
            if c==0:
                cur=i
            if i==cur:
                c+=1
            else:
                c-=1
        return cur

        
