# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast= head,head
        
        while(fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            
        slow = self.reverselist(slow)
        while(slow):
            if(slow.val != head.val):
                return False
            slow = slow.next
            head = head.next
        
        return True
    def reverselist(self,head):
        prev = None

        while(head):
            new_node = head.next
            head.next = prev
            prev = head
            head = new_node

        return prev
    