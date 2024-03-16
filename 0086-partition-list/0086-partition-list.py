# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1:ListNode = ListNode()
        list2:ListNode = ListNode()
        p1:ListNode = list1
        p2:ListNode = list2
        while head is not None:
            if head.val < x:
                p1.next = head 
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = list2.next
        p2.next = None
        return list1.next