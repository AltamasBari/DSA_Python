from collections import deque
class MyQueue:

    def __init__(self):
        self.st1 = deque()
        self.st2 = deque()
        

    def push(self, x: int) -> None:
        self.st1.append(x)
    def pop(self) -> int:
        if len(self.st2):
            return self.st2.pop()
        else:
            while self.st1:
                self.st2.append(self.st1.pop())
            return self.st2.pop()

    def peek(self) -> int:
        if len(self.st2):
            return self.st2[-1]
        else:
            while self.st1:
                self.st2.append(self.st1.pop())
            return self.st2[-1]

    def empty(self) -> bool:
        if len(self.st1) or len(self.st2):
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()