class Solution:
    def largestPrime(self, n: int) -> int:
        if n<2:
            return 0

        
        prime = [True] * (n+1)
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j]=False
        p=[i for i in range(2,n+1) if prime[i]]

        s=0
        res=0
        for ps in p:
            s+=ps
            if s>n:
                break
            if prime[s]:
                res=s
        return res
