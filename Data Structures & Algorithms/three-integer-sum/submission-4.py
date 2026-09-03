class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while left < right:
                s = nums[left] + nums[i] + nums[right]

                if s == 0:
                    result.append([nums[left], nums[i], nums[right]])
                    left = left + 1
                    right = right - 1

                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1
                elif s < 0:
                    left = left + 1
                else:
                    right = right - 1
        return result