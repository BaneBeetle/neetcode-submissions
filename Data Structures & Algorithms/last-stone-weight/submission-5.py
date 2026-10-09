import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []

        for stone in stones:
            heapq.heappush(self.heap, -stone)

        while len(self.heap) > 1:
            stone1 = heapq.heappop(self.heap)
            stone2 = heapq.heappop(self.heap)

            if stone1 != stone2:
                heapq.heappush(self.heap, -(max(-stone1, -stone2) - min(-stone1, -stone2)))

        if self.heap:
            return -self.heap[0]
        return 0

        
        