class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n, m=len(nums), 10**9+7
        f, p=Counter(nums), Counter()
        cnt=0
        p[nums[0]]+=1
        for i in range(1, n-1):
            x=nums[i]
            x2=x<<1
            cnt+=p[x2]*(f[x2]-p[x2]-(x==0))
            p[x]+=1
        return cnt%m
