class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        found = 0

        for i in range(len(nums)):
            if nums[i] == target:
                if target not in seen:
                    seen[target] = [i]
                else:
                    seen[target].append(i)
                found = 1
        if found == 0:
            return [-1,-1]
        elif len(seen[target]) == 1:
            return [seen[target][0], seen[target][0]]
        else:
            return [seen[target][0], seen[target][-1]]
        