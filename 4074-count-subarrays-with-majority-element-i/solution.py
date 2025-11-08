class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = nums

        arr = []
        for x in res:
            if x == target:
                arr.append(1)
            else:
                arr.append(-1)

        pre = 0
        freq = {0:1}
        ans = 0

        for v in arr:
            pre += v

            for p in freq:
                if p < pre:
                    ans += freq[p]

            freq[pre] = freq.get(pre,0) + 1

        return ans
