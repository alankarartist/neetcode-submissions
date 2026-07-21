import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            arr = nums.copy()
            arr.pop(i)
            x.append(math.prod(arr))
        return x