# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        nums = set()
            
        dummy.next = head
        pre = dummy
        curr = pre.next
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                while(curr.next and curr.val == curr.next.val):
                    curr = curr.next
                pre.next = curr.next
            else:
                pre = pre.next
            
            curr = curr.next

        return dummy.next