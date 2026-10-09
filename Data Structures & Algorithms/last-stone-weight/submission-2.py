class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []
        for weight in stones:
            max_heap.append(-weight)
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            lighter = -heapq.heappop(max_heap)

            if heaviest > lighter:
                remaining = heaviest - lighter
                heapq.heappush(max_heap, -remaining)
            

        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]