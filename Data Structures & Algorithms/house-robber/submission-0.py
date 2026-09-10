class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0

        for i in nums:
            third = max(second, first + i)
            first = second
            second = third
        
        return second