class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp = head
        next_node = head.next
        head.next = None

        while next_node:
            head = next_node
            next_node = next_node.next
            head.next = temp
            temp = head

        return head