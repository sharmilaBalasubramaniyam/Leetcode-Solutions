class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count=Counter(deck)
        a=0
        for v in count.values():
            a=math.gcd(a,v)
        return a>=2
