class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.capacity[i]

    def set(self, i: int, n: int) -> None:
        self.capacity[i] = n

    def pushback(self, n: int) -> None:
        capacity = len(self.capacity)
        if self.size == capacity:
            self.resize()
        self.set(self.size, n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.capacity[self.size]

    def resize(self) -> None:
        capacity = len(self.capacity) * 2
        arr = [None] * capacity
        for i in range(self.size):
            arr[i] = self.capacity[i]
        self.capacity = arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.capacity)
