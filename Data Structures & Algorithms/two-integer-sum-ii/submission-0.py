class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        x = []
        for i in range(n):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target and i < j:
                    x.append(i+1)
                    x.append(j+1)
        return x