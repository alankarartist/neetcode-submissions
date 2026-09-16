class TreeNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.map = None

    def insertHelper(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        if key < root.key:
            root.left = self.insertHelper(root.left, key, val)
        elif key > root.key:
            root.right = self.insertHelper(root.right, key, val)
        elif key == root.key:
            root.val = val
        return root

    def insert(self, key: int, val: int) -> None:
        self.map = self.insertHelper(self.map, key, val)

    def get(self, key: int) -> int:
        return self.search(self.map, key)

    def search(self, root, key):
        if not root:
            return -1
        
        if key > root.key:
            return self.search(root.right, key)
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return root.val

    def minValNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMin(self) -> int:
        curr = self.minValNode(self.map)
        if curr:
            return curr.val
        return -1

    def getMax(self) -> int:
        if not self.map:
            return -1
        curr = self.map
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.key:
            root.right = self.deleteNode(root.right, key)
        elif key < root.key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                minNode = self.minValNode(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.key)
        return root

    def remove(self, key: int) -> None:
        self.map = self.deleteNode(self.map, key)

    def inorderKeys(self, root):
        x = []
        if not root:
            return []
        x.extend(self.inorderKeys(root.left))
        x.append(root.key)
        x.extend(self.inorderKeys(root.right))
        return x

    def getInorderKeys(self) -> List[int]:
        return self.inorderKeys(self.map)