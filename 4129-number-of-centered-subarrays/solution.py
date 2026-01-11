class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            cs=0
            e=set()
            for j in range(i,n):
                cs+=nums[j]
                e.add(nums[j])
                if cs in e:
                    c+=1
        return c
