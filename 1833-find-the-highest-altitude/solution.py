class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        ma=0
        for g in gain:
            curr+=g
            ma=max(ma,curr)
        return ma
        
