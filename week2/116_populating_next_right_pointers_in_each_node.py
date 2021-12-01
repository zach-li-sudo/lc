class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # level order traversal, my sol
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        queue = collections.deque([([root], 1), ])
        while queue:
            node_list, level = queue.pop()
            if node_list:
                for i in range(len(node_list)):
                    if i in range(len(node_list)-1):
                        node_list[i].next = node_list[i+1] # populate next to the right node
                    else:
                        node_list[-1].next = None
                # if node_list[0].left is not None and node_list[0].right is not None:
                #     queue.appendleft(([node.left, node.right, for node in node_list], level+1))
                if node_list[0].left is not None and node_list[0].right is not None:
                    new_list = []
                    for node in node_list:
                        new_list.append(node.left)
                        new_list.append(node.right)
                    
                    queue.appendleft((new_list, level+1))
        return root

    # sol, recursive
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
