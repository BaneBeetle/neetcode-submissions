class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # Add all the numbers into the heap
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:

        if len(self.min_heap) == self.k:
            if val > self.min_heap[0]:
                heapq.heappop(self.min_heap) # Get rid of the smallest element
                heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)

        print(len(self.min_heap))
        return self.min_heap[0]
