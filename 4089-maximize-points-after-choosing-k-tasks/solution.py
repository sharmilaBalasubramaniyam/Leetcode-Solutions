class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n=len(technique1)
        t=sum(technique2)
        b=[technique1[i]-technique2[i] for i in range(n)]
        b.sort(reverse=True)
        for i in range(k):
            t+=b[i]

        for i in range(k,n):
            if b[i]>0:
                t+=b[i]
            else:
                break
        return t
