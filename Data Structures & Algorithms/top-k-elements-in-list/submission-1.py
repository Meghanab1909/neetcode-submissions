class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        with_count = []
        for i in count.keys():
            with_count.append([i, count[i]])
        
        with_count[:] = sorted(with_count, key = lambda x:x[1], reverse = True)

        result = []
        for i in with_count[:k]:
            result.append(i[0])
            
        return result