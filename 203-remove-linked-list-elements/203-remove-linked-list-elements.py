# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a_head = ListNode(0)
        res = a_head
        
        while head:
            if head.val != val:
                a_head.next = head
                a_head = a_head.next
                head = head.next
            else:
                head = head.next
        a_head.next = None            
        return res.next