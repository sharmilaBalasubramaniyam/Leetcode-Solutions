class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for s in sentences:
            cnt=len(s.split(" "))
            m=max(m,cnt)
        return m
