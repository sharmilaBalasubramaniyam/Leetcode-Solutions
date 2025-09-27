from collections import Counter
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)

        grp = {}

        for ch, f in freq.items():
            grp.setdefault(f,[]).append(ch)

        bf, bg = max(grp.items(), key = lambda x: (len(x[1]), x[0]))

        return "".join(bg)
