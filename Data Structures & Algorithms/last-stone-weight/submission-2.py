class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]
        elif len(stones) == 2:
            return abs(stones[1] - stones[0])
        else:
            h = []

            for i in stones:
                heapq.heappush(h, -i)
            
            print(h)
            while len(h) != 1:
                if len(h) != 0:
                    first = -heapq.heappop(h)
                    second = -heapq.heappop(h)

                    if first > second:
                        new_weight = first - second 
                        heapq.heappush(h, -new_weight)

                    print(h)
                else:
                    break

            if len(h) == 0:
                return 0
            return -h[0]