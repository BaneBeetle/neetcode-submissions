class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []

        # Add all the numbers into the heap
        for num in nums:
            heapq.heappush(self.max_heap, -num)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.max_heap, -val)

        # Now we need to find the third largest element
        heap_copy = []
        for e in self.max_heap:
            heapq.heappush(heap_copy, e)
        
        for v in range(self.k - 1):
            print("Hit")
            heapq.heappop(heap_copy)

        return -heapq.heappop(heap_copy)


        
