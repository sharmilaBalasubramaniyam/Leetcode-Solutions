class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        res = (num,sum)
        n,tot = res

        if tot > 9*n:
            return ""

        ans = []

        for i in range(n):
            dig = min(9,tot)
            ans.append(str(dig))
            tot -= dig

        return "".join(ans)
