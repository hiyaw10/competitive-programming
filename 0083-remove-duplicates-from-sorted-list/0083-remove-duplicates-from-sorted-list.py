# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            temp = head     
            while temp != None and temp.next != None:
                while temp.val == temp.next.val:
                    temp.next = temp.next.next
                    if temp.next == None:
                        break
                temp = temp.next
            return head