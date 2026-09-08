# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        nodes = []
        while p:
            nodes.append(p.val)
            p = p.next
        
        p = head
        index = -1

        while p:
            p.val = nodes[index]
            index = index - 1
            p = p.next
        
        return head

        