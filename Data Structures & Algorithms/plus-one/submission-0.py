class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        num = int(''.join(digits)) + 1
        return [i for i in str(num)]

