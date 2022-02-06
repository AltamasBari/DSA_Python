# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        mp = {}
        for elem in lists:
            while elem:
                mp[elem.val] = mp.get(elem.val,0) + 1
                elem = elem.next
        
        head = res = ListNode(0)
        for x in sorted(mp):
            for i in range(mp[x]):
                res.next = ListNode(x)
                res = res.next
        return head.next
        '''
        i = 0# Solving the PriorityQueue issue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            i += 1 # Solving the PriorityQueue issue
            if node: q.put((node.val,i,node))
        while q.qsize()>0:
            i += 1 # Solving the PriorityQueue issue
            curr.next = q.get()[2]
            curr=curr.next
            if curr.next: q.put((curr.next.val,i, curr.next))
        return dummy.next