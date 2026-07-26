class Solution:
    def __init__(self):
        self.x = set()
    def isHappy(self, n: int) -> bool:
        n = str(n)
        y = 0
        for i in n:
            y += int(i) ** 2
            
        if y == 1:
            return True
        if y not in self.x:
            self.x.add(y)
            return self.isHappy(y)
        else:
            return False