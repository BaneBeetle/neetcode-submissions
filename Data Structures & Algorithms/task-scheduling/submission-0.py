class Solution:

    from collections import Counter, heapq, deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)

        max_heap = [-freq for freq in frequency.values()]

        heapq.heapify(max_heap)

        queue = deque() # (value, when can I go again)

        time = 0

        while max_heap or queue:

            # pop from the maxheap Done
            # keep track of time Done
            # whenever we pop, popped value + 1 -> queue as well (t + n) = (value, when can I go again)
            # if popped value + 1 = 0, don't add it to the queue
            # if queue is not empty, but maxheap is empty, "idle"

            if max_heap:
                current_task = heapq.heappop(max_heap)

                current_task += 1

                if current_task < 0:
                    # current_task, time + n
                    queue.append((current_task, time + n))
            


            if queue and queue[0][1] <= time:
                heapq.heappush(max_heap, queue.popleft()[0])
            time += 1

        return time




