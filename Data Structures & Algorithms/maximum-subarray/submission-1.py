class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = float('-inf')

        for i in range(len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum)
            maxSum = max(maxSum, currentSum)
        
        return maxSum