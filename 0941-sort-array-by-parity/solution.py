class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oe=[]
        ee=[]
        for i in nums:
            if i%2 ==0:
                ee.append(i)

            if i%2 !=0:
                oe.append(i)

        res=ee+oe
        return res
        
