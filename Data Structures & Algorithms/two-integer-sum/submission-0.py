class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)):
            rem = target - nums[i]
            index = [j for j in range(i+1, len(nums)) if nums[j] == rem]
            if index:
                final.append(i)
                final.append(index[0])
        return final