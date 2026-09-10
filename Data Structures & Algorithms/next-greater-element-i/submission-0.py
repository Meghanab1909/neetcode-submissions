class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
                smaller = stack.pop()
                nextGreater[smaller] = i
            stack.append(i)
        
        while stack:
            smaller = stack.pop()
            nextGreater[smaller] = -1
        
        return [nextGreater[i] for i in nums1]
        