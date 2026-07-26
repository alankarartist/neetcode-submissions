class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = {}
        for i in nums:
            if i not in x:
                x[i] = 1
            else:
                x[i] += 1
        rev_x = {v: k for k, v in x.items()}
        return rev_x[1]