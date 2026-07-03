class Solution:
    def isPalindrome(self, s: str) -> bool:
        revers = ""

        for w in s:
            if w.isalnum():
                revers += w.lower()
        return revers == revers[::-1]