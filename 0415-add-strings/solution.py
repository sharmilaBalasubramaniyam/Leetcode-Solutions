class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #add1=int(num1)+int(num2)
        #return str(add1)

        
        s1 = list(num1)
        s2 = list(num2)

        carry = 0
        res = []

        while s1 or s2 or carry:
            d1 = ord(s1.pop()) - 48 if s1 else 0
            d2 = ord(s2.pop()) - 48 if s2 else 0

            total = d1 + d2 + carry
            res.append(str(total % 10))
            carry = total // 10
        
        return "".join(res[::-1])
