class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq=Counter(nums)
        fc=Counter(freq.values())
        for num in nums:
            if fc[freq[num]]==1:
                return num
        return -1
        
