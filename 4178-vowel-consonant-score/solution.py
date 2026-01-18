class Solution:
    def vowelConsonantScore(self, s: str) -> int:

        vow=set('aeiou')
        v=0
        c=0
        for ch in s:
            if 'a'<=ch<='z':
                if ch in vow:
                    v+=1
                else:
                    c+=1
        
        return v//c if c>0 else 0
        
