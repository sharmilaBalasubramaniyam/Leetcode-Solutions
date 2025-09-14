from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        if not tasks:
            raise ValueError("non empty")
        return min(u + m for u, m in tasks)
