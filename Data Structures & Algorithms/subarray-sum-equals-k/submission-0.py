class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        prefix_sum = 0

        for i in nums:
            prefix_sum += i

            if (prefix_sum - k) in hashmap:
                count += hashmap[prefix_sum - k]
            
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = 1
            else:
                hashmap[prefix_sum] += 1
        
        return count

        