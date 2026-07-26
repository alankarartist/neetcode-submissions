class MedianFinder:

    def __init__(self):
        self. x = []

    def addNum(self, num: int) -> None:
        self.x.append(num)
        self.x.sort()

    def findMedian(self) -> float:
        n = len(self.x)
        if n % 2 == 0:
            return (self.x[n//2] + self.x[n//2 - 1]) / 2
        return self.x[n//2]