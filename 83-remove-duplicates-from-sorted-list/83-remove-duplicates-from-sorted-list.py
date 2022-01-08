# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = head
        a_point = prev
        cur = head.next
        
        while cur:
            if prev.val == cur.val:
                cur = cur.next
            else:
                prev.next = cur
                prev = prev.next
                cur = cur.next
        prev.next = None
        return a_point
        