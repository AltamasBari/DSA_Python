# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and head.next is None:
            return head
        '''
        1 2 3 4
        
        0
        '''
        
        new_list = ListNode(0)
        new_head = new_list
        
        
        def reverse(head):
            prev = None
            k = 2
            while(head and k):
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                k -= 1
            return prev
        
        while(head):
            prev = head
            tail = head
            k = 2
            while(tail and k):
                k -= 1
                tail = tail.next
            if k==0:
                new_head.next = reverse(prev)
                new_head = prev
            elif k != 0:
                new_head.next = prev
            
            head = tail
        
        return new_list.next
                