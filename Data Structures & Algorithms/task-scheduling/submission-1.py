from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks) # Count the tasks

        heap = [-v for v in counts.values()]
        heapq.heapify(heap) # Heap creation

        queue = deque([])
        ret = 0

        while heap or queue:
            ret += 1
            if queue:
                if queue[0][1] == ret:
                    task = queue.popleft()
                    heapq.heappush(heap, task[0])
            
            if heap:
                current = -heapq.heappop(heap)
                current -= 1
                if current > 0:
                    queue.append((-current, ret + n + 1))
            
        
        return ret
