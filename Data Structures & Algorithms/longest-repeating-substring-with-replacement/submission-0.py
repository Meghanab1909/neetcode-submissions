class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        count = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            
            maxFreq = max(maxFreq, count[s[right]])

            while  ((right - left + 1) - maxFreq) > k:
                count[s[left]] -= 1
                left = left + 1
            
            result = max(result, (right - left + 1))
        
        return result