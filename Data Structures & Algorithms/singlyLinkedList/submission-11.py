class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        c = 0
        curr = self.head.next
        while curr:
            if c == index:
                return curr.data
            c += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
    
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr
