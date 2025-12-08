class Solution:
    def countTriples(self, n: int) -> int:
        cnt=0
        ns=int(sqrt(n))
        for s in range(2, ns+1):
            for t in range((s&1)+1, s, 2):
                if gcd(s,t)!=1: continue
                c=s*s+t*t
                if c>n: break
                k=n//c
                cnt+=2*k
        return cnt
        
