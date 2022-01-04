# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
sol 1. time o(n), space o(n)
'''
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        array.sort()
        print(array)

        dummy = ListNode(0)
        new_head = dummy
        for val in array:
            node = ListNode(val)
            new_head.next = node
            new_head = new_head.next

        return dummy.next


'''
sol 2: 
'''
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass