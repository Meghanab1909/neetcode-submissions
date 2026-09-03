class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
            
        nums[:] = sorted(list(set(nums)))
        curLength = 1
        maxLength = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                maxLength = max(maxLength, curLength)
                curLength = 1
            else:
                curLength += 1
        
        maxLength = max(maxLength, curLength)
        return maxLength
