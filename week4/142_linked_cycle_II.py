def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    visited = set()
    while head:
        if head not in visited:
            visited.add(head)
            head = head.next
        else:
            return head
    return None