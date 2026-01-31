class Solution:
    def grayCode(self, n: int) -> List[int]:
        it=1<<n
        res=[0]*it
        for x in range(it):
            res[x]=x^(x>>1)
        return res

        
