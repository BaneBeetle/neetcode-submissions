# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #(node's Value, i, node)
        
        heap = []
        dummy = ListNode()
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        current = dummy
        while heap:
            tup = heapq.heappop(heap) # (node's value, i, node)

            current.next = tup[2]
            current = current.next

            if tup[2].next:
                heapq.heappush(heap, (tup[2].next.val, tup[1], tup[2].next))

     
        return dummy.next


