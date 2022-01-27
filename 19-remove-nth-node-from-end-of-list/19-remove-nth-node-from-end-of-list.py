# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if(head == None): return head
        
        
        count = 0
        temp = head
        while(temp):
            count += 1
            temp = temp.next
        i = 0
        itr = ListNode(0,None)
        point = itr
        itr.next = head
        while(head and i < (count-n)):
            itr.next = head
            itr = itr.next
            head = head.next
            i += 1
                
        if(itr.next.next):
            itr.next = itr.next.next
        else:
            itr.next = None
        
        return point.next
'''