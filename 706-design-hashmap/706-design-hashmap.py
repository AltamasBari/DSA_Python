class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 769
        self.map = [None]*self.size

    def put(self, key: int, value: int) -> None:
        bucket = key % self.size
        if self.map[bucket] == None:
            self.map[bucket] = ListNode(key, value)
        else:
            cur = self.map[bucket]
            while True:
                if cur.key == key:
                    cur.value = value #update
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket = key % self.size
        head = self.map[bucket]
        while head:
            if head.key == key:
                return head.value
            else:
                head = head.next
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.size
        cur = prev = self.map[bucket]
        if not cur: return
        if cur.key == key:
            self.map[bucket] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)