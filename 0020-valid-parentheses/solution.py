class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        b = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in b:
                t= st.pop() if st else '#'
                if b[ch] != t:
                    return False
            else:
                st.append(ch)
        return not st
