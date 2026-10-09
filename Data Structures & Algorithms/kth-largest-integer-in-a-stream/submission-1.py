class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []

        # Add all the numbers into the heap
        for num in nums:
            if len(self.max_heap) == self.k:
                if num > self.max_heap[0]:
                    heapq.heappop(self.max_heap)
                    heapq.heappush(self.max_heap, num)

            else:
                heapq.heappush(self.max_heap, num)
        

    def add(self, val: int) -> int:

        if len(self.max_heap) == self.k:
            if val > self.max_heap[0]:
                heapq.heappop(self.max_heap) # Get rid of the smallest element
                heapq.heappush(self.max_heap, val)
        else:
            heapq.heappush(self.max_heap, val)

        print(len(self.max_heap))
        return self.max_heap[0]
