class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        
        merged = [intervals[0]]

        for i in intervals[1:]:
            start = i[0]
            end = i[1]

            last = merged[-1]

            if start <= last[1]:
                merged[-1][-1] = max(end, last[1])
            else:
                merged.append([start, end])
        
        return merged
        