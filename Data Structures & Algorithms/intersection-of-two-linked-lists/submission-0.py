# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = []
        p = headA

        while p:
            listA.append(p)
            p = p.next
        
        q = headB
        found = 0

        while q:
            if q in listA:
                return q
                found = 1
                break
            q = q.next
        
        if found == 0:
            return None
