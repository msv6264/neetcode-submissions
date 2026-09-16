# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        res = ListNode(0)
        tail = res
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = ListNode(p1.val)
                p1 = p1.next

            else:
                tail.next = ListNode(p2.val)
                p2 = p2.next

            tail = tail.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        return res.next