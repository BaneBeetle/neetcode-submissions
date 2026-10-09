# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1_smallest = list1
        l2_smallest = list2

        head = None
        current = head

        while (l1_smallest != None) or (l2_smallest != None):
            print('ran')
            if head is None:
                if l1_smallest != None and l2_smallest != None:
                    if l1_smallest.val <= l2_smallest.val:
                        head = ListNode(l1_smallest.val)
                        l1_smallest = l1_smallest.next
                    else:
                        # happens when l1 is bigger
                        head = ListNode(l2_smallest.val)
                        l2_smallest = l2_smallest.next
                    current = head
                # What if one of them is none?
                elif l1_smallest != None:
                    print("L1 none head")
                    return l1_smallest
                else:
                    # this means l1 has to be none
                    print("L2 none head")
                    return l2_smallest



            # is l1 None? If so dump L2
            if l1_smallest is None:
                temp = ListNode(l2_smallest.val)
                current.next = temp
                l2_smallest = l2_smallest.next
                current = temp

            # is L2 None? If so, dump L1
            elif l2_smallest is None:
                print("l2 is none")
                temp = ListNode(l1_smallest.val)

                current.next = temp
                l1_smallest = l1_smallest.next
                current = temp

            # That means both L1 and L2 are not None yet
            elif l1_smallest.val <= l2_smallest.val:
                temp = ListNode(l1_smallest.val)
                current.next = temp
                l1_smallest = l1_smallest.next
                current = temp
            else:
                # happens when l1 is bigger
                temp = ListNode(l2_smallest.val)
                current.next = temp
                l2_smallest = l2_smallest.next
                current = temp

        print(head)
        return head

        