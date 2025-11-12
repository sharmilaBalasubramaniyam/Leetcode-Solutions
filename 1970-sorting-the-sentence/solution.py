class Solution:
    def sortSentence(self, s: str) -> str:
        word=s.split()
        word.sort(key= lambda x:int(x[-1]))
        word=[x[:-1] for x in word]
        return " ".join(word)
