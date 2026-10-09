class Solution:
    import heapq
    from math import sqrt

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ret = []
        minheap = []

        for coords in points:
            x = coords[0] 
            y = coords[1]

            distance = math.sqrt((x)**2 + (y)**2)
            minheap.append([distance, coords])
        
        heapq.heapify(minheap)

        for x in range(k):
            popped = heapq.heappop(minheap)
            ret.append(popped[1])
        
        return ret
