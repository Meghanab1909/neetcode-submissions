class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                cleaned += i.lower()
        return cleaned == cleaned[-1::-1]
        