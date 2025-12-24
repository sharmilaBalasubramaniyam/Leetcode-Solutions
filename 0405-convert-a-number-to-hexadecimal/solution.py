class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        else:
            hm="0123456789abcdef"
            res=""
            num=num & 0xFFFFFFFF

            while num > 0:
                res=hm[num & 15]+res
                num >>= 4
            
            return res

                
