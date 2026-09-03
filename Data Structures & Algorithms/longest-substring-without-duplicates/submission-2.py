class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLength = 0

        for i in s:
            if i in substring:
                maxLength = max(maxLength, len(substring))
                substring = substring[substring.index(i)+1:]
            substring += i
            
        maxLength = max(maxLength, len(substring))
        return maxLength