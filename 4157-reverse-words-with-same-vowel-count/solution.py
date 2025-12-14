class Solution:
    def reverseWords(self, s: str) -> str:
        vow=set("aeiouAEIOU")
        def c_vow(w:str)->int:
            return sum(1 for ch in w if ch in vow)

        ws=s.split()
        if not ws:
            return s

        tar=c_vow(ws[0])

        def res_w(w:str)->str:
            return w[::-1]

        for i in range(1,len(ws)):
            if c_vow(ws[i])==tar:
                ws[i]=res_w(ws[i])
                
        return " ".join(ws)
