from collections import defaultdict

class Solution:
    def countPairs(self, words: List[str]) -> int:
        def n(word):
            b=ord(word[0])-ord('a')
            p=[]
            for ch in word:
                d=(ord(ch)-ord('a')-b)%26
                p.append(d)
            return tuple(p)

        freq=defaultdict(int)
        c=0
        for word in words:
            key=n(word)
            c+=freq[key]
            freq[key]+=1
        return c
        
