# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headB or not headA:
            return None
        
        pA = headA
        pB = headB
        lastA = 0
        lastB = 0
        
        while pA != pB:
            if lastB != 0 and lastA != 0 and lastA != lastB:
                    return None
            if not pA.next:
                lastA = pA
                pA = headB
            else:
                pA = pA.next
            if not pB.next:
                lastB = pB
                pB = headA
            else:
                pB = pB.next
            
        return pA
            