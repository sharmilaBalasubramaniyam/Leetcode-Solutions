class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        val=[-i for i in nums]
        heapq.heapify(val)
        for i in range(k-1):
            heapq.heappop(val)
        
        return -heapq.heappop(val)
        
