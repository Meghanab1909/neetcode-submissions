class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = 0
        currentSum = 0

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                currentSum -= nums[left]
                minLength = min(minLength, right - left + 1)
                left = left + 1
        
        return minLength if minLength != float('inf') else 0