class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''s=str(x)
        return s==s[::-1]'''

        if x<0:
            return False

        ori=x
        rev=0

        while x!=0:
            dig=x%10
            rev=rev*10+dig
            x//=10

        return ori==rev

