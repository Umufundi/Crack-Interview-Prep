class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MRUQueue:

    def __init__(self, n: int):
        self.head = ListNode(0, None)
        curr = self.head
        for i in range(1, n+1):
            curr.next = ListNode(i, None)
            curr = curr.next
        self.tail = curr

    def fetch(self, k: int) -> int:
        curr = self.head
        while k > 1:
            curr = curr.next
            k -= 1

        mru = curr.next
        if curr.next.next:
            curr.next = curr.next.next
            self.tail.next = mru
            self.tail = self.tail.next
            mru.next = None
        return mru.val