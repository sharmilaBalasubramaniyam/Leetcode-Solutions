class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            n = num
            while n > 0:
                s += n % 10
                n //= 10
            num = s
        return num


        
