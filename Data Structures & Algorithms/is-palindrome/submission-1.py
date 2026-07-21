class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for i in s.lower():
            if i.isalnum():
                word += i
        return word == word[::-1]