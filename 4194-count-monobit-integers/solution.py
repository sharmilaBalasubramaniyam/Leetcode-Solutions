class Solution:
    def countMonobit(self, n: int) -> int:
        c=1
        v=1
        while v<=n:
            c+=1
            v=(v<<1)|1
        return c
        
        
