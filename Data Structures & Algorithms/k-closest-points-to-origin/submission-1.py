import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (-distance, coordinate)
        heap = [((p[0]**2 + p[1]**2), p) for p in points]
        heapq.heapify(heap)

        ret = []

        counter = 0
        while counter < k:
            ret.append(heapq.heappop(heap)[1])
            counter += 1
            

        return ret


