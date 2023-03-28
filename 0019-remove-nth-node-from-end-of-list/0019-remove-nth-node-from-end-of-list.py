class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Store = []
        cur = head
        while cur:
            Store.append(cur.val)
            cur = cur.next
        N = len(Store) - n
        Store.pop(N)
        
        dum = ListNode(None)
        cur = dum
        for num in Store:
            new = ListNode(num)
            cur.next = new
            cur = cur.next
        return dum.next