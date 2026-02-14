class Solution:
    
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for w in words:
            t=0
            for ch in w:
                t+=weights[ord(ch)-ord('a')]
            mv=t%26
            mc=chr(ord('z')- mv)
            res+=mc
        return res
        
