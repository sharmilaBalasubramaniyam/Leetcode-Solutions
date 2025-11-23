class Solution:
    def sumAndMultiply(self, n: int) -> int:
        dig=[d for d in str(n) if d!='0']
        if not dig:
            return 0
        x=int(''.join(dig))
        ds=sum(int(d) for d in dig)
        return x*ds
        
