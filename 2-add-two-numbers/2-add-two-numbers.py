# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = ListNode()
        res_head = res
        rem = 0
        
        while l1 and l2:
            
            sm = (l1.val + l2.val + rem) % 10
            rem = (l1.val + l2.val + rem) // 10
            
            temp = ListNode(sm)
            
            res.next = temp
            res = res.next
            l1 = l1.next
            l2 = l2.next
            
        while(l1):
            sm = (l1.val + rem) % 10
            rem = (l1.val + rem) // 10

            temp = ListNode(sm)

            res.next = temp
            res = res.next
            l1 = l1.next
        

        while(l2):
            sm = (l2.val + rem) % 10
            rem = (l2.val + rem) // 10

            temp = ListNode(sm)

            res.next = temp
            res = res.next
            l2 = l2.next
        
        if rem:
            temp = ListNode(rem)
            res.next = temp
        
        return res_head.next
        
            