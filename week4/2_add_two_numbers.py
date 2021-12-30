class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nodelist):
        pass

    def __str__(self):
        pass



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        result = ListNode(0)
        head = result

        carry = 0
        res = 0
        while h1 or h2:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            digit_sum = val1 + val2 + carry
            res = digit_sum % 10
            result.val = res

            carry = digit_sum // 10
                
            h1 = h1.next if h1 and h1.next else None
            h2 = h2.next if h2 and h2.next else None
            result.next = ListNode(carry)
            result = result.next
        
        result = head
        while result.next:
            if result.next.val == 0 and result.next.next is None:
                result.next = None
            else:
                result = result.next

        return head



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(s % 10) # current digit
            tail = tail.next
            carry = s // 10 # carry for next digit
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next