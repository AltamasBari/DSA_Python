# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        head = new_head

        while (l1 != None and l2 != None):

            if(l1.val > l2.val):
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next

            head = head.next

        if(l1 != None):
            head.next = l1

        if(l2 != None):
            head.next = l2 

        return new_head.next