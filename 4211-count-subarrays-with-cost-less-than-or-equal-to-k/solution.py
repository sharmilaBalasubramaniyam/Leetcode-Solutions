class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        miq=deque()
        maq=deque()

        l=0
        res=0

        for r in range(len(nums)):
            while miq and miq[-1]>nums[r]:
                miq.pop()
            miq.append(nums[r])

            while maq and maq[-1]<nums[r]:
                maq.pop()
            maq.append(nums[r])

            while(maq[0]-miq[0]) * (r-l+1)>k:
                if nums[l]==miq[0]:
                    miq.popleft()
                if nums[l]==maq[0]:
                    maq.popleft()
                l+=1
            res+=r-l+1
        return res
