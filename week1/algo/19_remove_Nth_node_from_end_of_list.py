class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        length = 0
        first = head
        while first:
            first = first.next
            length += 1
        
        length -= n # index of node to remove
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        
        # link the later to former of target node
        first.next = first.next.next
        return dummy.next



