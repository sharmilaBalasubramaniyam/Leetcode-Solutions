class Solution:
    def rob(self, nums: List[int]) -> int:
#            n=len(nums)
#            ec=0
#            oc=0
#           for i in range(0,n):
 #               if i%2==0:
  #                  ec+=nums[i]
   #             else:
    #                oc+=nums[i]
     #       return max(ec,oc)
        p1,p2=0,0
        for i in nums:
            cur=max(p1,p2+i)
            p2,p1=p1,cur
        return cur
    


        
