class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.h = []

        for i in nums:
            self.add(i)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        if len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]
        
