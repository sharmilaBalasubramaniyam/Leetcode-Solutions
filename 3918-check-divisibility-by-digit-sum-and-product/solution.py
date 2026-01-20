class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        s=0
        p=1

        while temp>0:
            digit=temp%10
            s+=digit
            p*=digit
            temp//=10
        
        total=s+p
        
        return n%total==0
        
