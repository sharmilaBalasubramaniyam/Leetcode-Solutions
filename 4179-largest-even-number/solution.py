class Solution:
    def largestEven(self, s: str) -> str:
        if not s:
            return ""
        ltw=s.rfind('2')
        return s[:ltw+1]
