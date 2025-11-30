from collections import Counter
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        freq = Counter(nums)

        uni = sorted(freq.keys())

        tot = n

        max = {}

        suff = 0

        for i in reversed(uni):
            max[i] = suff
            suff += freq[i]

        ans = 0
        for x in nums:
            if max[x] >= k:
                ans += 1

        return ans
