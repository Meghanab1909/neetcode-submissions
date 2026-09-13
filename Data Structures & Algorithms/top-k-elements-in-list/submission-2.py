class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        arr_with_freq = [(x, count[x]) for x in count]
        arr_with_freq.sort(key = lambda x:x[1], reverse=True)
        
        result = []
        for i in arr_with_freq[:k]:
            result.append(i[0])
        
        return result
        