class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is the second half of head
        # reverse slow:
        rev_slow = self.rev_ll(slow)
        # compare rev_slow to the first half of head, node by node
        while rev_slow:
            if rev_slow.val != head.val:
                return False
            rev_slow = rev_slow.next
            head = head.next
        return True
        
    # reverse a linked list
    def rev_ll(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return cur