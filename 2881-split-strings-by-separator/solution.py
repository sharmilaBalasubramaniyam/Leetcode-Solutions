class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res=[]

        for s in words:
            par=s.split(separator)
            for p in par:
                if p !='':
                    res.append(p)
        return res
