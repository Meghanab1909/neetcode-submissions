class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i in strs:
            cleaned = "".join(sorted(list(i)))
            if cleaned not in group:
                group[cleaned] = [i]
            else:
                group[cleaned].append(i)
        
        result = []
        for i in group.keys():
            result.append(group[i])
        
        return result
        