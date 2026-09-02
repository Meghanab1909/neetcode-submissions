class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums[:] = sorted(list(set(nums)))
        maxLength = 0
        currentLength = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                maxLength = max(maxLength, currentLength)
                currentLength = 1
            else:
                currentLength += 1
        
        maxLength = max(maxLength, currentLength)
        return maxLength
        