class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            prev = head
            curr = head.next
            newhead = head.next
        else:
            return head
        
        while curr and curr.next:
            # swap nodes
            prev.next = curr.next
            curr.next = prev
            # swap pointers
            curr, prev = prev, curr
            # move next
            curr = curr.next.next
            prev = prev.next.next
            
        return newhead
