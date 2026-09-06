class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while i < k:
            end = nums.pop()
            nums.insert(0, end)
            i = i + 1
        
