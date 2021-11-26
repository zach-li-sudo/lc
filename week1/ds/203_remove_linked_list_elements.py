class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newhead = head
        if head is None:
            return head

        while head and head.val == val:
            head = head.next
            newhead = head
        
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
                continue
            head = head.next
            
        return newhead