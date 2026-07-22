class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        triplets = []
        value_to_indices = defaultdict(list)
        for i in range(len(nums)):
            value_to_indices[nums[i]].append(i)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                remaining = target - nums[i] - nums[j]
                indexes = [k for k in value_to_indices[remaining] if k > j]
                sub_triplet = [[nums[i],nums[j],nums[k]] for k in indexes]
                triplets.extend(sub_triplet)
        triplets.sort()
        distinct_triplets = {tuple(sorted(sublist)) for sublist in triplets}
        result = [list(triplet) for triplet in distinct_triplets]
        return result

