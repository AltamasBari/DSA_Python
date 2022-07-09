# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head 
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(node):
            prev = None
            while(node):
                next_node = node.next
                node.next = prev
                
                prev = node
                node = next_node
            
            return prev
        
        node2 = slow.next
        node2 = reverse(node2)
        slow.next = None
        prev = ListNode(0)
        prev_head = prev
        
        while(node2):
            prev.next = head
            prev = prev.next
            head = head.next
            
            prev.next = node2
            prev = prev.next
            node2 = node2.next
        
        while(head):
            prev.next = head
            prev = prev.next
            head = head.next 
        
        return prev_head.next