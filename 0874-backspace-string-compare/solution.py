class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def b(st):
            stack = []
            for ch in st:
                if ch != '#':
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)
        
        return b(s) == b(t)

