class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        max_count = 0
        for i in range(len(nums)):
            if i+1 <= len(nums)-1:
                if nums[i+1] == nums[i] + 1:
                    count += 1
                elif nums[i+1] == nums[i]:
                    count += 0
                else:
                    if max_count < count:
                        max_count = count
                    count = 1
        if max_count < count:
            max_count = count
        return max_count