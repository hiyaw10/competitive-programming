class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store = []
        root = head
        while root:
            store.append(root)
            root = root.next
        s = len(store)-n
        if len(store)>1:
            if s==0:
                head=head.next
                return head
            elif s!=0 and (s+1)<len(store):
                store[s-1].next = store[s+1]
                return head
            else:
                store[s-1].next = None
                return head
        else:
            return 