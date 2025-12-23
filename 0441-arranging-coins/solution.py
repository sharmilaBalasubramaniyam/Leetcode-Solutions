class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = int((-1 + math.sqrt(1 + 8 * n)) // 2)
        return k
