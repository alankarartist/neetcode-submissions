class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        x = []
        for i in nums:
            if i not in x:
                x.append(i)
            else:
                flag = True
        return flag