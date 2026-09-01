class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        array_with_count = []
        for i in count:
            array_with_count.append([i, count[i]])
        
        array_with_count.sort(key = lambda x:x[1], reverse = True)
        
        return [x[0] for x in array_with_count[:k]]