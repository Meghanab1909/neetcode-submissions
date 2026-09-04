class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        maxString = ""
        
        for left in range(len(s)):
            for right in range(left, len(s)):
                substring = s[left:right+1]

                if substring == substring[-1::-1]:
                    if len(substring) > len(maxString):
                        maxString = substring
        return maxString