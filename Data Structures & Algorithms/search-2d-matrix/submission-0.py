class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = None
        for i in matrix:
            if target in i:
                return True
        return False
        