class Solution:
    def minimumFlips(self, n: int) -> int:
        bi=bin(n)[2:]
        flips=0
        l,r=0,len(bi)-1
        while l<r:
            if bi[l]!=bi[r]:
                flips+=2
            l+=1
            r-=1
        if l==r:
            pass
        return flips
        
        return flips
