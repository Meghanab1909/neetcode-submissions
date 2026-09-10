class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums[:] = sorted(list(set(nums)))
        longest_seq = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                longest_seq = max(longest_seq, current)
                current = 1
            else:
                current += 1
        
        longest_seq = max(longest_seq, current)

        return longest_seq


        