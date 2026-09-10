class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        
        while i < k:
            end = nums.pop()
            nums[:] = [end] + nums
            i = i + 1
        
        print(nums)
            