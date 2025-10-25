class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        small = s

        for i in range(1,n+1):
            res = s[:i][::-1]+s[i:]
            if res < small:
                small = res

        for i in range(1,n+1):
            res = s[:-i]+s[-i:][::-1]
            if res < small:
                small = res
        return small
