class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        prehead = ListNode(-1)
        returned_head = prehead
        i = list1
        j = list2

        while i and j:
            if i.val <= j.val:
                prehead.next = i
                i = i.next
                prehead = prehead.next
            else:
                prehead.next = j
                j = j.next
                prehead = prehead.next
        
        while i:
            prehead.next = i
            i = i.next
            prehead = prehead.next

        while j:
            prehead.next = j
            j = j.next
            prehead = prehead.next
        
        return returned_head.next
                
