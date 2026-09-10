# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        nodes = []

        while p:
            nodes.append(p.val)
            p = p.next
        
        left = 0
        right = len(nodes)-1

        result = []
        while left <= right:
            result.append(nodes[left])
            result.append(nodes[right])
            left = left + 1
            right = right - 1

        p = head
        index = 0

        while p:
            p.val = result[index]
            p = p.next
            index = index + 1