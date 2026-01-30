class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq={}

        for n in nums:
            freq[n]=freq.get(n,0)+1
            if freq[n]>2:
                return False
        return True

