# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head

        # find head
        if curr.next.val != head.val:
            pass
        else:
            while curr.next.val == curr.val:
                curr = curr.next
            curr = curr.next
            head = curr
        
        prev = head
        current_value = curr.val
        curr = curr.next

        while curr is not None:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                while curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
            prev.next = curr



                
        
        return head
