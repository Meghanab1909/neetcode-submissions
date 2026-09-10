class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maximum = 0

        for i in s:
            if i in substring:
                maximum = max(maximum, len(substring))
                substring = substring[substring.index(i)+1:]
            substring += i
            
        maximum = max(maximum, len(substring))
        return maximum

        