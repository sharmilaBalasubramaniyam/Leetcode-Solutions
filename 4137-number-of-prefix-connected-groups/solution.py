class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        pc={}
        for w in words:
            if len(w)>=k:
                p=w[:k]

                if p in pc:
                    pc[p]+=1
                else:
                    pc[p]=1
        grp=0
        for c in pc.values():
            if c>=2:
                grp+=1
        return grp
        
