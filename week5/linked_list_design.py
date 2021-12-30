class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        # return -1 for invalid index
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        dummy = ListNode(val)
        dummy.next = self.head
        self.head = dummy

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val:int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        new_node = ListNode(val)
        new_node.next = pred.next
        pred.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1

        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        pred.next = pred.next.next