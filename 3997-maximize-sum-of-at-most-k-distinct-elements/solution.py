class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        u=list(set(nums))
        u.sort(reverse=True)
        return u[:k]
