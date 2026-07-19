class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        arr = [[y,x] for x, y in dict1.items()]
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
