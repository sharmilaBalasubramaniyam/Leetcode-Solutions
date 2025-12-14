class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

       # maxk=0
       # mink=0
        #for i in nums:
        #    if(i>maxk):
        #        maxk+=i
        #    else:
        #        mink+=i

        nums.sort()
        mink=sum(nums[:k])
        maxk=sum(nums[-k:])
        return abs(maxk-mink)
            
