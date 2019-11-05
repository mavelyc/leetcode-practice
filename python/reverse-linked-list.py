# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):

        ########### Recusively ###################
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

        ############ Iteratively ################
        # curr = head
        # prev = None
        
        # while curr != None:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tmp
        
        # return prev