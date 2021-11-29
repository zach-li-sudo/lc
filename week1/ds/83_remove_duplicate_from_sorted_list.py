# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        newhead = head
        prev = head

        while head.next is not None:
            if head.next.val == prev.val:
                head = head.next.next
                prev.next = head
                prev = head
            else:
                head = head.next
                prev = head
            
            if head is None:
                break

        return newhead
