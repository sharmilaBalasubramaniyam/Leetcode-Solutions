class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1

        while(n!=0):
            d=n%10
            p*=d
            s+=d
            n//=10
        
        return p-s
        
