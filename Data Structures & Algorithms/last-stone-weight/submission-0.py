class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []
        for weight in stones:
            heapq.heappush(max_heap, -weight)

        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            lighter = -heapq.heappop(max_heap)

            difference = heaviest - lighter
            if difference == 0:
                continue
            else:
                heapq.heappush(max_heap, -difference)
        
        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]