# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        pointer1 = head
        pointer2 = head
        
        while pointer2 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        return pointer1

        