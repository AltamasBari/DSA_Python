# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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