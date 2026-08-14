class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def isEmpty(self) -> bool:
        return self.head.next is None

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        else:
            self.tail = node
        self.head.next = node
        node.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        head_node = self.head.next
        next_node = head_node.next
        self.head.next = next_node
        if next_node:
            next_node.prev = self.head
        else:
            self.tail = self.head
        return head_node.val