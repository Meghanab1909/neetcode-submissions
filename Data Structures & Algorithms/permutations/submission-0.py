class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return
            
            for i in nums:
                if i not in current:
                    current.append(i)
                    backtrack()
                    current.pop()
        backtrack()
        return result