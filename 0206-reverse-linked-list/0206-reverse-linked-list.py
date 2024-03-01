# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        current = head.next
        previous = head
        head.next = None
        
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            
        return previous

            
        