class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        tot = 0
        while temp != None:
            tot += 1
            temp = temp.next
        mid = tot // 2 
        temp2 = head
        for i in range(mid-1):
            temp2 = temp2.next
        head = temp2.next
        return head