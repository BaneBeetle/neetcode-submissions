class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]

        heapq.heapify(maxheap)

        for i in range(k - 1):
            heapq.heappop(maxheap)
        
        return -heapq.heappop(maxheap)