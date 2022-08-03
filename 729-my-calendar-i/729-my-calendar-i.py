class MyCalendar:

    def __init__(self):
        self.mp = {}

    def book(self, start: int, end: int) -> bool:
        for s2,e2 in self.mp.items():
            if not (start >= e2 or s2 >= end):
                return False
        
        self.mp[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)