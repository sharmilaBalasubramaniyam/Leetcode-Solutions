class Solution:
    def frequencySort(self, s: str) -> str:
        heap=[]
        for x,y in Counter(s).items():
            heap.append((-y,x))
        heapq.heapify(heap)
        res=""
        while heap:
            i=heapq.heappop(heap)
            res+=i[1]*(-i[0])
        return res
