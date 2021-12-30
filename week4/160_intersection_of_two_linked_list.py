class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     visited_A = set()
    #     visited_B = set()
    #     while headA or headB:
    #         if headA in visited_B:
    #             return headA
    #         elif headA:
    #             visited_A.add(headA)
    #             headA = headA.next
    #         if headB in visited_A:
    #             return headB
    #         elif headB:
    #             visited_B.add(headB)
    #             headB = headB.next
    #     return None

    # hashtable, time comp O(M+N) in worst case, space comp o(M+N)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = set()
        while headA or headB:
            if headA in visited_nodes:
                return headA
            elif headA:
                visited_nodes.add(headA)
                headA = headA.next
            if headB in visited_nodes:
                return headB
            elif headB:
                visited_nodes.add(headB)
                headB = headB.next
        return None

    # two pointers, time comp O(M+N) in worst case, space comp o(1)


    
