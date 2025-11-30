class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        n = len(nums)
        ans = n

        prefix = 0
        last = {0: -1}

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            target = (prefix - r) % p

            if target in last:
                ans = min(ans, i - last[target])
            last[prefix] = i

        return ans if ans < n else -1
